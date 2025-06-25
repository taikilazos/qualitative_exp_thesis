import streamlit as st
import json
import random

# Set page config
st.set_page_config(
    page_title="Text Simplification Rating",
    page_icon="📝",
    layout="wide"
)

# Load texts from JSON file
@st.cache_data
def load_texts():
    try:
        with open('texts_data.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        st.error("texts_data.json file not found. Please make sure the file exists.")
        return None

# Title
st.title("Text Simplification Rating System")

# Load data
data = load_texts()
if data is None:
    st.stop()

abstracts = data['abstracts']

# Initialize session state for ratings and version mapping if not exists
if 'ratings' not in st.session_state:
    st.session_state.ratings = {}
    
if 'version_mapping' not in st.session_state:
    st.session_state.version_mapping = {}

if 'action_ratings' not in st.session_state:
    st.session_state.action_ratings = {}

# Initialize version mapping and ratings for all abstracts
for abstract_key in abstracts.keys():
    if abstract_key not in st.session_state.version_mapping:
        versions = list(abstracts[abstract_key]['versions'].keys())
        random.shuffle(versions)
        st.session_state.version_mapping[abstract_key] = {
            f"Simplified Version {i+1}": version 
            for i, version in enumerate(versions)
        }
    
    if abstract_key not in st.session_state.ratings:
        st.session_state.ratings[abstract_key] = {}

# Initialize ratings for all action tasks
action_tasks = data.get('action_based_tasks', {})
for task_key in action_tasks.keys():
    if task_key not in st.session_state.action_ratings:
        st.session_state.action_ratings[task_key] = {}

# Display each abstract consecutively
for abstract_key, abstract_data in abstracts.items():
    st.header(f"📄 {abstract_data['title']}")
    
    current_mapping = st.session_state.version_mapping[abstract_key]
    current_ratings = st.session_state.ratings[abstract_key]
    
    # Show completion status
    completed_ratings = len(current_ratings)
    st.write(f"Progress: {completed_ratings}/5 versions rated")
    if completed_ratings == 5:
        st.success("✅ All versions rated!")
    
    # Create columns for original and simplified texts
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Original Text")
        st.text_area(
            "Original", 
            abstract_data['original'], 
            height=300, 
            disabled=True,
            key=f"original_{abstract_key}"
        )
    
    with col2:
        st.subheader("Simplified Versions")
        
        # Display each simplified version with rating
        for display_name, actual_version in current_mapping.items():
            with st.expander(f"{display_name} {'⭐' if display_name in current_ratings else ''}", expanded=display_name not in current_ratings):
                st.text_area(
                    f"{display_name} Text", 
                    abstract_data['versions'][actual_version], 
                    height=200, 
                    disabled=True,
                    key=f"text_{abstract_key}_{display_name}"
                )
                
                # Rating system
                st.write("Rate this version (1-5):")
                current_rating = current_ratings.get(display_name, None)
                
                # Create rating buttons in a single row
                rating_cols = st.columns(5)
                for rating in range(1, 6):
                    with rating_cols[rating-1]:
                        if st.button(
                            str(rating), 
                            key=f"{abstract_key}_{display_name}_{rating}",
                            type="primary" if current_rating == rating else "secondary"
                        ):
                            st.session_state.ratings[abstract_key][display_name] = rating
                            st.rerun()
                
                # Display current rating
                if current_rating:
                    st.write(f"Your rating: {current_rating} ⭐")
    
    # Show ratings summary for this abstract
    if current_ratings:
        st.write("**Your ratings for this abstract:**")
        rating_summary_cols = st.columns(5)
        for i, (display_name, rating) in enumerate(current_ratings.items()):
            with rating_summary_cols[i % 5]:
                st.write(f"{display_name}: {rating}⭐")
    
    st.divider()

# Action-based tasks
st.header("📝 Action-based Task Rating")
for task_key, task_data in action_tasks.items():
    st.subheader(f"🧩 {task_data['title']}")

    st.markdown("**Prompt Instructions:**")
    st.text_area(
        "", 
        task_data['prompt_instructions'], 
        height=150, 
        disabled=True,
        key=f"instructions_{task_key}"
    )

    st.markdown("**Text to Simplify:**")
    st.text_area(
        "", 
        task_data['text_to_simplify'], 
        height=100, 
        disabled=True,
        key=f"text_{task_key}"
    )

    st.markdown("**Output:**")
    st.text_area(
        "", 
        task_data['output'], 
        height=100, 
        disabled=True,
        key=f"output_{task_key}"
    )

    # Rating system
    st.write("Rate how well the output follows the prompt (1-5):")
    current_rating = st.session_state.action_ratings.get(task_key, None)
    
    # Create rating buttons in a single row
    rating_cols = st.columns(5)
    for rating in range(1, 6):
        with rating_cols[rating-1]:
            if st.button(
                str(rating), 
                key=f"{task_key}_{rating}",
                type="primary" if current_rating == rating else "secondary"
            ):
                st.session_state.action_ratings[task_key] = rating
                st.rerun()
    
    # Display current rating
    if current_rating:
        st.write(f"Your rating: {current_rating} ⭐")

    st.divider()

# Overall progress summary
st.header("📊 Overall Progress")
total_abstract_ratings = len(abstracts) * 5
total_action_ratings = len(action_tasks)
total_possible_ratings = total_abstract_ratings + total_action_ratings

submitted_abstract_ratings = sum(len(ratings) for ratings in st.session_state.ratings.values())
submitted_action_ratings = sum(1 for r in st.session_state.action_ratings.values() if r is not None)
total_submitted_ratings = submitted_abstract_ratings + submitted_action_ratings

progress = total_submitted_ratings / total_possible_ratings if total_possible_ratings > 0 else 0
st.progress(progress)
st.write(f"Overall Progress: {total_submitted_ratings}/{total_possible_ratings} ratings completed ({progress:.1%})")

# Progress by abstract
progress_cols = st.columns(len(abstracts))
for i, (abstract_key, abstract_data) in enumerate(abstracts.items()):
    with progress_cols[i]:
        abstract_ratings = st.session_state.ratings.get(abstract_key, {})
        completed = len(abstract_ratings)
        st.metric(
            label=abstract_data['title'],
            value=f"{completed}/5",
            delta=f"{(completed/5)*100:.0f}% complete"
        )

# Export ratings button
st.header("💾 Export Results")
if st.button("Export All Ratings", type="primary"):
    if any(st.session_state.ratings.values()) or any(st.session_state.action_ratings.values()):
        # Create comprehensive export data
        export_data = {
            "total_ratings": total_submitted_ratings,
            "total_possible": total_possible_ratings,
            "completion_percentage": progress,
            "timestamp": str(st.session_state.get('timestamp', 'unknown')),
            "abstracts": {},
            "action_based_tasks": {}
        }
        
        for abstract_key, abstract_data in abstracts.items():
            abstract_ratings = st.session_state.ratings.get(abstract_key, {})
            abstract_mapping = st.session_state.version_mapping.get(abstract_key, {})
            
            export_data["abstracts"][abstract_key] = {
                "title": abstract_data['title'],
                "ratings": abstract_ratings,
                "version_mapping": {
                    display_name: {
                        "actual_version": actual_version,
                        "rating": abstract_ratings.get(display_name)
                    }
                    for display_name, actual_version in abstract_mapping.items()
                },
                "completion": f"{len(abstract_ratings)}/5",
                "completion_percentage": (len(abstract_ratings)/5)*100
            }

        action_ratings = st.session_state.get('action_ratings', {})
        for task_key, task_data in action_tasks.items():
            export_data["action_based_tasks"][task_key] = {
                "title": task_data['title'],
                "rating": action_ratings.get(task_key)
            }
        
        st.download_button(
            label="📥 Download All Ratings as JSON",
            data=json.dumps(export_data, indent=2),
            file_name="text_simplification_ratings.json",
            mime="application/json"
        )
    else:
        st.warning("Please submit some ratings first.") 