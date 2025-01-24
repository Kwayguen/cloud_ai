
import streamlit as st
import pandas as pd
import seaborn as sns
import os
import matplotlib.pyplot as plt

st.set_page_config(
    page_title='Streamlit',
    page_icon="🔫",
    layout='wide'
)

# upload file
uploaded_file = st.file_uploader("Choose a file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, delimiter=",")
    selected_columns = st.multiselect("Selectionner les colonnes du dataframe", df.columns)
    edited_df = st.data_editor(df[selected_columns])
    
if uploaded_file is not None:
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Configuration du graphique")
        
        chart_type = st.selectbox(
            "Choisir le type de graphique à afficher",
            ("Bar Chart", "Line Chart", "Scatter Plot")
        )

        x_axis = st.selectbox("Sélectionner la colonne pour l'axe X", selected_columns)
        reverse_x = st.checkbox("Inverser l'axe X", key="reverse_x")
        y_axes = st.multiselect(
            "Sélectionner les colonnes pour l'axe Y", 
            selected_columns, 
            default=selected_columns
        )
        reverse_y_options = {}
        for y in y_axes:
            reverse_y_options[y] = st.checkbox(
                f"Inverser l'axe Y pour '{y}' (Line/Scatter uniquement)",
                key=f"reverse_y_{y}"
            )

        
        
    
    with col2:
        st.subheader("Action")
        if st.button("Afficher le Graphique"):
            if not y_axes:
                st.error("Veuillez sélectionner au moins une colonne pour l'axe Y.")
            else:
                st.write("Graphique généré :")
                
                fig, ax = plt.subplots(figsize=(6,4))  # Adjust size as needed
                color_palette = sns.color_palette(n_colors=len(y_axes))

                # ------------------
                #     BAR CHART
                # ------------------
                if chart_type == "Bar Chart":
                    # Melt all chosen Y columns
                    edited_df_melt = edited_df.melt(
                        id_vars=x_axis, 
                        value_vars=y_axes, 
                        var_name='Variable', 
                        value_name='Valeur'
                    )
                    
                    # Single call to barplot with hue='Variable'
                    sns.barplot(
                        data=edited_df_melt,
                        x=x_axis,
                        y='Valeur',
                        hue='Variable',
                        ax=ax,
                        errorbar=None
                    )
                    
                    # Since a single bar chart uses one Y-axis,
                    # we cannot invert the Y-axis individually per column.
                    # If you want to invert the entire Y-axis (all columns),
                    # you can add a single checkbox for the bar chart, e.g.:
                    # if st.checkbox("Inverser l'axe Y (Bar Chart)"):
                    #     ax.invert_yaxis()

                # ------------------
                #    LINE CHART
                # ------------------
                elif chart_type == "Line Chart":
                    for idx, y in enumerate(y_axes):
                        sns.lineplot(
                            data=edited_df,
                            x=x_axis,
                            y=y,
                            label=y,
                            ax=ax,
                            color=color_palette[idx]
                        )
                        
                        # Invert Y (only for this column) if requested
                        if reverse_y_options[y]:
                            ax.invert_yaxis()

                # ------------------
                #   SCATTER PLOT
                # ------------------
                elif chart_type == "Scatter Plot":
                    for idx, y in enumerate(y_axes):
                        sns.scatterplot(
                            data=edited_df,
                            x=x_axis,
                            y=y,
                            label=y,
                            ax=ax,
                            color=color_palette[idx]
                        )
                        
                        # Invert Y (only for this column) if requested
                        if reverse_y_options[y]:
                            ax.invert_yaxis()
                
                # Invert X-axis if requested (applies to all columns)
                if reverse_x:
                    ax.invert_xaxis()
                
                plt.tight_layout()
                st.pyplot(fig)
        
        if edited_df is not None:
            st.download_button(
            label="download data as csv",
            data=edited_df.to_csv(),
            file_name="df.csv",
            mime="text/csv"
        )









