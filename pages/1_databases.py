import streamlit as st
import pandas as pd
# from streamlit_extras.great_tables import great_tables
# from great_tables import GT
from Utils.utils import get_years, make_html_table_from_dataframe, replace_semicolon_with_linebreak, get_all_column_values



class dashboard:
    def __init__(self):
        self.title = "ILUTE Group Data Sources"
        self.icon = "dashboard"
        self.data = pd.read_excel('Data_dictionary_full_edited.xlsx', sheet_name='Dataset Overview')
        self.data['Start Year'] = pd.to_numeric(self.data['Start Year'], errors='coerce').astype('Int64')
        self.data['End Year']   = pd.to_numeric(self.data['End Year'],   errors='coerce').astype('Int64')

    def sidebar(self):
        st.sidebar.title(self.title)
        
        
        st.sidebar.markdown(
            "This dashboard provides an overview of the datasets used in the ILUTE group research. "
            "You can filter the datasets by year using the slider on the left."
        )

        # Year selection
        min_start, max_end = get_years(self.data['Start Year'], self.data['End Year'])
        self.years = st.sidebar.slider("Select Years", min_start, max_end, (min_start, max_end), step=1)

        # Spatial selection
        spatial_options = get_all_column_values(self.data['Coverage'])
        self.spatial_options = st.sidebar.multiselect("Select Geographical Scope", spatial_options, default=spatial_options)

        # Select tags
        tags = get_all_column_values(self.data['Tags'])
        self.selected_tags = st.sidebar.multiselect("Select Tags", tags, default=tags)

    def table(self):
        # from great_tables import GT
        # st.subheader("Dataset Overview")
        self.filtered_data = self.data.copy()
        if self.years: 
            self.filtered_data = self.data[
                (self.data['Start Year'] >= self.years[0]) & (self.data['End Year'] <= self.years[1])
            ]

        if self.spatial_options:
            self.filtered_data = self.filtered_data[
                self.filtered_data['Coverage'].isin(self.spatial_options)
            ]

        if self.selected_tags:
            self.filtered_data = self.filtered_data[
                self.filtered_data['Tags'].apply(lambda x: any(tag in x for tag in self.selected_tags))
            ]
        # table = (
            # GT(self.filtered_data)
            # .tab_header("Dataset Overview")
            #     )
        # great_tables(table, width="content")
        st.markdown(make_html_table_from_dataframe(self.filtered_data), unsafe_allow_html=True)


    def render(self):
        st.title(self.title)
        st.write("This is the dashboard page.")
        self.sidebar()
        self.table()


if __name__ == "__main__":
    dashboard().render()