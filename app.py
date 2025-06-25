import streamlit as st
import json
import random

# Set page config
st.set_page_config(
    page_title="Text Simplification Rating",
    page_icon="📝",
    layout="wide"
)

# Title
st.title("Text Simplification Rating System")

# Define the texts
texts = {
    "Original": """Background: The purpose of the study was to examine whether early repeated infections due to Trichomonas vaginalis among human immunuodeficiency virus (HIV)-positive and HIV-negative women are reinfections, new infections, or cases of treatment failure.
Methods: Women attending an HIV outpatient clinic and a family planning clinic in New Orleans, Louisiana, who had culture results positive for T. vaginalis were treated with 2 g of metronidazole under directly observed therapy.
At 1 month, detailed sexual exposure and sexual partner treatment information was collected.
Isolates from women who had clinical resistance (i.e., who tested positive for a third time after treatment at a higher dose) were tested for metronidazole susceptibility in vitro.
Results: Of 60 HIV-positive women with trichomoniasis, 11 (18.3%) were T. vaginalis positive 1 month after treatment.
The 11 recurrences were classified as 3 probable reinfections (27%), 2 probable infections from a new sexual partner (18%), and 6 probable treatment failures (55%); 2 of the 6 patients who experienced probable treatment failure had isolates with mild resistance to metronidazole.
Of 301 HIV-negative women, 24 (8.0%) were T. vaginalis positive 1 month after treatment.
The 24 recurrences were classified as 2 probable reinfections (8%) and 22 probable treatment failures (92%); of the 22 patients who experienced probable treatment failure, 2 had strains with moderate resistance to metronidazole, and 1 had a strain with mild resistance to metronidazole.
Conclusion: HIV-positive women were more likely to have sexual re-exposure than were HIV-negative women, although the rate of treatment failure was similar in both groups.
High rates of treatment failure among both HIV-positive and HIV-negative women indicate that a 2-g dose of metronidazole may not be adequate for treatment of some women and that rescreening should be considered.""",

    "Version_A": """For the study's background, the study's aim was to find whether early repeated infections of Trichomonas vaginalis (a parasite that can cause a sexually transmitted infection or STI) among women with human immunuodeficiency virus (HIV) and without HIV are reinfections, new infections, or cases of treatment failing.
For the study's methods, women attending an HIV clinic and family planning clinic in New Orleans, Louisiana, who had tests detecting T. vaginalis, were treated with 2 grams (g) of metronidazole (an antibiotic for infections) under directly observed treatment.
At 1 month, we collected detailed sexual activity and sexual partner treatment information.
Samples from women who had clinical resistance (i.e., who had tests detecting T. vaginalis for a third time after treatment at a higher dose) were tested for metronidazole sensitivity.
Of 60 women with HIV and trichomoniasis, 11 (18.3%) had T. vaginalis 1 month after treatment.
The 11 recurrences were grouped as 3 possible reinfections (27%), 2 possible infections from a new sexual partner (18%), and 6 possible treatment failures (55%). 2 of the 6 patients with possible treatment failure had samples with mild resistance to metronidazole.
Of 301 women without HIV, 24 (8%) had tests detecting T. vaginalis 1 month after treatment.
The 24 recurrences were grouped as 2 possible reinfections (8%) and 22 possible treatment failures (92%). Of the 22 patients with possible treatment failure, 2 had samples with medium resistance to metronidazole. 1 had a sample with mild resistance to metronidazole.
In conclusion, women with HIV were more likely to have sexual re-exposure than were women without HIV. However, the rate of treatment failure was similar in both groups.
High rates of treatment failure among both women with and without HIV indicate that a 2-g dose of metronidazole may not the best treatment of some women and that retesting should be considered.""",

    "Version_B": """The goal of this research is to figure out what happens when many people get infected again by an STI called trichomoniasis in both those who have AIDS and do not have it.
Women from two clinics received treatment at this place because they tested positive for Trichomonas vaginalis using cultures; each woman was given 2000 milligrams of Metronidazol while being watched by healthcare workers during their visit.
At age of 30 days, we asked about their sex life in detail including who they had been intimate with recently.
Women whose bodies resisted antibiotic treatments, which they took three times as much of than usual, showed that their bacteria could still be killed by another medicine called metronizadole when it was put on them outside of people's bodies.
Of sixty HIV-infected females who had been treated for an infection called Trichomonas vaginitis, eleven of them tested positive again just over four weeks later.
The eleven cases included three possible re-infections, two likely infections acquired through sex partners, six failed treatments where five people showed some antibiotic weakness against Metronidazol.
Of 301 healthy women who didn't have AIDS virus infection, about eight percent had Trichomonas parasite in their vagina one month later when they finished taking medicine for it.
The 24 cases included two possible infections from outside sources that happened again after initial recovery, twenty-two failed treatments where bacteria did not respond well enough to medication; among those whose treatments didn't work properly for them, only three people's bacterial samples showed some level of antibiotic drug weakness - specifically, two moderately resistant ones and another mildly weak against an antibacterial called Metronidazol.
HIV positive females are at higher risk for future infections compared to those who don't carry this virus; however their chances of not responding well to medication aren't significantly different from non-infected individuals.
High levels of unsuccessful treatments in both infected and uninfected females suggest using more than two grams of this antibiotic might sometimes fail, so re-testing is recommended.""",

    "Version_C": """The goal is to figure out what happens when people get infected again by this type of bacteria called trachomona's vaginallis  , which can happen even after they have gotten better because either it came back through there sexual partener as a re-infection from them,or got another infeciton on its own, or maybe the cure didnt work for some reason so now we need to find out why.
Women from clinics attended by people living with AIDS and those seeking birth control services received treatment after testing positive for a parasite causing STDs; this included taking two grams of antibiotics while being watched as you swallow them.
At 1-month follow-up, detailed _______________  and _____________  information were collected.
Samples of bacteria taken from women that have been treated three times without success using an even stronger version are grown in the laboratory to find out whether they can survive when exposed to this particular type of antibiotic.
Results of testing showed that among sixty people living with AIDS who had contracted an STD caused by T.
The 11 relapses were classified into three categories; first there was twenty-seven percent that resulted from nineteen percent being infected by someone else for the second time while fifty-five percent showed signs indicating that antibiotics like amoxicillin weren't effective against bacterial growth within them so two out of six people whose treatments didn't work at all tested positive on lab tests using only small amounts of an antibacterial drug called antibiotic which they took regularly but still developed symptoms due to resistant bacteria strains present inside those particular individuals' bodies.
Of 301 women who do not have AIDS virus infection, 8% had an STD caused by a parasite called Trichomonas vaginalis 30 days later when they received their medication for it.
The 24 relapses were classified into two categories - eight percent being repeat infections from their partners and ninety-two percent having treatments that are likely failing; among those whose treatments aren't working there was an individual infected by parasites resistant at low levels to antibiotics such as amoxicillin but also another person suffering due to bacteria which is only slightly less effective against this particular type of medication known commonly used for treating bacterial vaginosis caused mainly when certain types of sexually transmitted diseases occur including chlamydia gonorrhea trichomoniasis etc.
HIV-positive women are more likely than HIV-negative ones to be exposed again thru sex; however their rates for treatments that aren't working remain equal.
Antibiotic use has high levels of treatment not being effective amongst those who are positive as well as negative; therefore it is recommended you give them an extra two grams which isn't always sufficient so they might need another round of tests done again.""",

    "Version_D": """The goal of this research is to determine why some people infected by Trichamonias get reinfected again after being treated for it.
Women from two clinics received treatment after testing positive for Trichomonas infection; they took 2000 milligrams of antibiotic medication while being watched by healthcare workers during their visits.
At 1-month follow-up visit, we asked for details about their recent sex life and what treatments were given to any of those they had recently been intimate with.
Women who didn't respond well enough to an increased dosage of their medication, which they took three times when previously treated, showed that certain bacteria did not react as expected to another specific medicine during lab tests.
Of 60 women living with AIDS who had an infection called trichomoniases caused by Trichomonas vaginale, eleven percent became infected again within thirty days of receiving medication.
The 11 times when symptoms came back again, they could be due to either having sex with someone else that gave them an infection  cases, not taking medication correctly leading to relapse , or failing on their prescribed antibiotic regimen which made it harder for this particular drug to work against bacteria found inside two out of six people experiencing such issues whose test results showed very slight signs of being resistant to said medicine.
Of ___________ women who did not have AIDS virus infection, _______% had Trichomonas vaginale bacteria detected 1 week later than their therapy ended.
The 24 times when symptoms came back again were mostly due to not responding well enough to medication; out of those cases where people didn't respond at all, some bacteria developed slight changes that made them harder for medicine called metronida-zole to work against, but most just got worse despite it.
HIV-infected females had higher rates of repeated exposure compared to those without infection; however their cure success remained equal for each group.
High rates of failed treatments suggest using more than two grams of this antibiotic might help, so it's worth retesting those who didn't respond well enough.""",

    "Version_E": """The goal of this research is to determine what causes frequent repeat occurrences of an infection caused by Trichamonias vaginallis among both HIV-positive and negative females - either they get it again after being treated previously, contract it for the first time despite previous treatments, or their current condition does not respond well to medication.
Women from two clinics in New York received treatment after testing positive for Trichomonas infection; they took 2000 milligrams of antibiotic medication while being closely monitored by healthcare workers during their visits.
At 1-month follow-up, we gathered complete details about each participant's recent sex life and their partners' treatments.
Women whose bodies did not respond well enough to high doses of an antibiotic called metronodizole, which they took three times when it was prescribed again, showed that their bacteria could still grow even though this medicine is usually effective against them because some strains are resistant inside lab tests using petri dishes.
Of 60 women who have both HIV/AIDS and an infection called trichomoniassis caused by Trichomonas vaginallis, eleven had it still at that time when they got treated for their condition one month later.
The 11 times when symptoms came back again, they could be due either to having sex with someone else that gave them an infection  cases, being infected by something other than their original cause , or not responding well enough to medication so it didn't work properly for those people .
Of ___________ women who did not have AIDS virus infection, _______% had Trichomonas vaginale bacteria still active 1 week/month/after/two weeks later/afterwards after being treated.
The 24 times when symptoms came back again were mostly due to not responding well enough to medication; among those people, some developed bacteria that didn't work against an antibiotic called metronida-zole very effectively.
HIV-infected females had higher rates of repeated exposure compared to those without infection; however their cure success remained equal for each group.
High rates of failed treatments suggest using more than two grams of this antibiotic might help, so it's best to retest those who didn't respond well initially."""
}

# Initialize session state for ratings and version mapping if not exists
if 'ratings' not in st.session_state:
    st.session_state.ratings = {}
    
if 'version_mapping' not in st.session_state:
    # Create a mapping between actual versions and displayed versions
    versions = ["Version_A", "Version_B", "Version_C", "Version_D", "Version_E"]
    random.shuffle(versions)
    st.session_state.version_mapping = {
        f"Simplified Version {i+1}": version 
        for i, version in enumerate(versions)
    }
    # Store reverse mapping for export
    st.session_state.reverse_mapping = {
        v: k for k, v in st.session_state.version_mapping.items()
    }

# Create columns for the layout
col1, col2 = st.columns([1, 1])

with col1:
    st.header("Original Text")
    st.text_area("Original", texts["Original"], height=400, disabled=True)

with col2:
    # Create tabs for different simplified versions using anonymous labels
    tabs = st.tabs(list(st.session_state.version_mapping.keys()))
    
    for display_name, actual_version in st.session_state.version_mapping.items():
        with tabs[list(st.session_state.version_mapping.keys()).index(display_name)]:
            st.text_area(display_name, texts[actual_version], height=300, disabled=True)
            
            # Rating system
            st.write("Please rate this simplified version (1-5):")
            
            # Create columns for rating buttons
            rating_cols = st.columns(5)
            
            # Get current rating from session state
            current_rating = st.session_state.ratings.get(display_name, None)
            
            # Create rating buttons
            for rating in range(1, 6):
                with rating_cols[rating-1]:
                    if st.button(
                        str(rating), 
                        key=f"{display_name}_{rating}",
                        type="primary" if current_rating == rating else "secondary"
                    ):
                        st.session_state.ratings[display_name] = rating

            # Display current rating
            if current_rating:
                st.write(f"Your rating: {current_rating} ⭐")

# Display all ratings at the bottom
st.header("Your Ratings Summary")
if st.session_state.ratings:
    for display_name, rating in st.session_state.ratings.items():
        st.write(f"{display_name}: {rating} ⭐")
else:
    st.write("No ratings submitted yet.")

# Export ratings button
if st.button("Export Ratings"):
    if st.session_state.ratings:
        # Create export data with both display names and actual versions
        export_data = {
            "ratings": st.session_state.ratings,
            "version_mapping": {
                display_name: {
                    "actual_version": actual_version,
                    "rating": st.session_state.ratings.get(display_name)
                }
                for display_name, actual_version in st.session_state.version_mapping.items()
            }
        }
        st.download_button(
            label="Download Ratings as JSON",
            data=json.dumps(export_data, indent=2),
            file_name="text_ratings.json",
            mime="application/json"
        )
    else:
        st.warning("Please submit some ratings first.") 