import streamlit as st
from Scrappy import scrape_jobs
def main():
    st.markdown("<h1 class='title'>Srappy!!</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Hey there! I’m Scrapy, created by Shiv 😎. I’m here to help you find and save jobs with all the details in a CSV file 🤖.</p>", unsafe_allow_html=True)

    # Multiselect optionsS
    site_name_options = ["linkedin","indeed", "glassdoor","zip_recruiter"] #, "zip_recruiter"
    selected_site_names = st.multiselect("Select job sites", site_name_options)

    # Text fields
    search_term = st.text_input("Job Title", "software engineer")
    location = st.text_input("Location", "Delhi, India")
    results_wanted = st.text_input("total results wanted", "10")
    country_indeed = st.text_input("Country for indeed/glassdoor", "India")

    if st.button("Scrape Jobs"):
        with st.spinner("Scraping jobs..."):
            jobs = scrape_jobs(
                site_name=selected_site_names,
                search_term=search_term,
                location=location,
                results_wanted=int(results_wanted),
                country_indeed=country_indeed
            )

            count = f"Found {len(jobs)} jobs"
            jobs.to_csv("jobs.csv", index=False)

            st.write(count)
            st.write("First 5 results:")
            st.dataframe(jobs.head())
            st.write("All results:")

            # Download button
            st.download_button(
                label="Download jobs.csv",
                data=jobs.to_csv(index=False).encode(),
                file_name="jobs.csv",
                mime="text/csv"
            )
        jobs = scrape_jobs(
            site_name=selected_site_names,
            search_term=search_term,
            location=location,
            results_wanted=int(results_wanted),
            country_indeed=country_indeed
        )

if __name__ == "__main__":
    main()



# print(f"Found {len(jobs)} jobs")
# print(jobs.head())
# jobs.to_csv("jobs.csv", index=False) # to_xlsx