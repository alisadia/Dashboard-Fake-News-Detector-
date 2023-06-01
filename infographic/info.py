from datetime import date
from turtle import width
import matplotlib.pyplot as plt
from numpy import real
import pandas as pd
import plotly.express as px
import seaborn as sns
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import altair as alt

# Page layout
st.set_page_config(page_title='FAKE NEWS DETECTOR',
                   layout='wide',
                   page_icon='fake.png')

hide_st_style = """
            <style>

           #fake-news-detector
           {
             padding:0px;
           }
            .css-zt5igj.e16nr0p32
            {
              font-size:25px;
              background-color: white;
              padding:5px 0 11px 50px;
              color:#008080;
              border-top: 2px solid #81a981;


            }
            .css-18ni7ap.e8zbici2
            {
              visibility:hidden;
            }
            .css-9s5bis.edgvbvh3
            {
              visibility:hidden;
            }
            .css-qri22k.egzxvld0
            {
              visibility:hidden;
            }
            .block-container.css-18e3th9.egzxvld2
            {
              padding:0 ;
            }
           .css-kswft9
           {
            gap:0;,#12343b
           }
            .appview-container.css-1wrcr25.egzxvld4
            {

              background-image:linear-gradient(#485e48,#648464,#81a981,#8FBC8F,#B6BC8F);
              #position:relative;
            }
             .css-1pt7fhu.e1tzin5v0
            {
              gap:0;
            }
            .css-ocqkz7.e1tzin5v4
            {
              gap:0;
            }


            .css-16nrs4v.e1tzin5v0
            {
              width:0;
            }

            .css-1offfwp p
            {
               margin:20px 0 20px 0;
               text-align: center;
               font-weight:bold;
               font-size:40px;
            }

            .css-1r6slb0.e1tzin5v2
            {

              background:rgba( 255, 255, 255, 0.25 );
              backdrop-filter: blur( 0.4px );
              border-radius: 10px;
              border: 1px solid rgba( 255, 255, 255, 0.25 );
              align-items:center;

            }
            .element-container.css-87sjgi.e1tzin5v3
            {
              height:0;
            }
            .main-svg
             {
              margin-left:30px;
              margin-top:30px;
               background:rgba( 255, 255, 255, );
              border: 1px solid rgba( 255, 255, 255, 0.25 );
              text-align:center;
              border-radius:10px;

             }
             .css-1r6slb0.e1tzin5v2
             {
              background:none;
              border:none;
              margin:50px 10px 50px 7px;

             }
             .css-ocqkz7.e1tzin5v4
             {
             margin-left:10px;
             }
             .css-j5r0tf
             {
                # margin:100px 10px 0 7px;

                # padding:10px 10px 10px 70px;
              background:rgba( 255, 255, 255, 0.25 );
              backdrop-filter: blur( 0.4px );
              border-radius: 10px;
              border: 1px solid rgba( 255, 255, 255, 0.25 );
              align-items:center;
             }

             .css-wnm74r.e16fv1kl0
             {
                font-size:18px;
                color:black;
             }
             .css-186pv6d.e16fv1kl2
             {
               font-size:20px;

             }
             .css-4inboy
             {
                text-align:center;
                width:40px;
             }
             .css-1ard3yh
             {
             align-items:center;
             text-align:center;
             background:red;
             width:100px;
             margin-left:20px;
             padding-left:10px;
             }
             .css-1offfwp
             {
              color:white;
              font-size:18px;
             }
             .css-12w0qpk
             {
             margin-top:100px;
              background:rgba( 255, 255, 255, 0.25 );
              backdrop-filter: blur( 0.4px );
              border-radius: 10px;
              border: 1px solid rgba( 255, 255, 255, 0.25 );
              align-items:center;
              margin-right:15px;
             }
             .css-50ug3q
             {}
             
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


col1, col2 = st.columns(2)
with col1:

    st.title("FAKE NEWS DETECTOR")

with col2:
    selected = option_menu(
        menu_title=None,
        options=["2018", "2019", "2020", "2021", "2022","2023", "Home"],
        orientation="horizontal",
        icons=["2018", "2019", "2020", "2021", "2022","2023", "Home"],
        default_index=6,
        styles={
            "container": {"padding": "0 0 0 0", "background-color": "white", "width": "100%", "margin": "0 0 0 0", "border-radius": "0", "border-top": "2px solid #81a981 "},
            "nav": {
                "gap": "5px",
                "margin-right": "50px",

            },

            "nav-link": {
                "color": "black",
                "font-weight": "bold",
                "font-size": "16px",
                "text-align": "center",
                "margin-right": "20px",
                "padding": "6px",
                "--hover-color": "#81a981",
                "transition": "1s",
                "border-radius": "5px",
                "box-shadow": "3px 3px 3px #81a981",
                "border-shadow": "",
            },
            "nav-link-selected": {"background-color": " #81a981"},
        },

    )


# Reading Csv/excel datset files

Re = pd.read_excel("Detection_Real_4040.xlsx")
df = pd.read_excel("Detection_Fake_1120.xlsx")  # Fake News dataset
df_combine = pd.concat([Re, df])
column1, column2 = st.columns(2)
if (selected == '2018'):

    # dividing page into columns
    
   
    Re['date'] = pd.to_datetime(Re['Published_ Date'], format='%Y-%m-%d')
    year_2018_Real= Re.loc[(Re['date'] >= '2018-01-01')
                   & (Re['date'] <= '2018-12-31')]
   
    with column1:
        fig_p = px.pie(data_frame=year_2018_Real, names='Party_Affiliation', width=600, height=500, title='<b>FIG 1.1: Pie Chart of Party Related to Real News</b>',
                       color_discrete_sequence=px.colors.qualitative.Bold_r)
        fig_p.update_layout(title_x=0.5, )
        fig_p.update_traces(textfont_size=16,)
        st.plotly_chart(fig_p)

        fig_bar = px.bar(data_frame=year_2018_Real, y='Source', labels={'count': "<b>Count of News(1 box=1 Unit)</b>", "Source": "<b>Channels</b>"},
                         color_discrete_sequence=px.colors.qualitative.Dark24_r,height=500, width=600, title='<b>FIG 2.1:Bar Chart of Channels which provided Real News</b>', color='Source')
        fig_bar.update_layout(
            title_x=0.5,
            xaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            yaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
           
        )
        st.plotly_chart(fig_bar)

        fig_pie = px.pie(data_frame=year_2018_Real, names='Subject', width=600, height=500, hole=0.4, title='<b>FIG 3.1: Donut Chart of Types of Politics of Real News</b>',
                         color_discrete_sequence=px.colors.sequential.Agsunset,)
        fig_pie.update_traces(textfont_size=16,)
        fig_pie.update_layout(
            title_x=0.5,)
        st.plotly_chart(fig_pie)

        fig_scatter = px.scatter(data_frame=year_2018_Real, x='Author', color='Author', labels={
            "Author": "<b>Author</b>",
            "index": "<b>Count of Max News provided by Author</b>"
        }, title="<b>FIG 4.1: Scatter Graph of Author which provided Real News</b>", height=500, width=600)
        fig_scatter.update_layout(
            title_x=0.5,
            xaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            yaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            plot_bgcolor='rgb(243, 243, 243)',
        )
        st.plotly_chart(fig_scatter)

        fig_area = px.bar(year_2018_Real, y="Location",  labels={
            "Location": "<b>Location</b>",
                          "count": "<b>Count of News at specific Location</b>",
                          }, title="<b>FIG 5.1: Bar Chart of Real News at Specific Location<b>", height=500, width=600, color_discrete_sequence=px.colors.sequential.Brwnyl_r)
        fig_area.update_layout(
            title_x=0.5,
            xaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            yaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            plot_bgcolor='rgb(243, 243, 243)',
        )
        st.plotly_chart(fig_area)

    with column2:
        df['date'] = pd.to_datetime(df['Published_ Date'], format='%d-%m-%Y')
        year_2018_fake = df.loc[(df['date'] >= '01-01-2018')
                   & (df['date'] <= '31-12-2018')]
        fig_p = px.pie(data_frame=year_2018_fake, names='Party_Affiliation', width=600, height=500, title='<b>FIG 1.2: Pie Chart of Party Related to Fake News</b>',
                       color_discrete_sequence=px.colors.qualitative.Bold)
        fig_p.update_layout(title_x=0.5, )
        fig_p.update_traces(textfont_size=16,)
        st.plotly_chart(fig_p)

        fig_bar = px.bar(data_frame=year_2018_fake, y='Source', labels={'count': "<b>Count of News(1 box=1 Unit)</b>", "Source": "<b>Channels</b>"},
                         height=500, width=600, title='<b>FIG 2.2: Bar Chart of Channels which provided Fake News</b>', color='Source')
        fig_bar.update_layout(
            title_x=0.5,
            xaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            yaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            plot_bgcolor='rgb(243, 243, 243)',
        )
        st.plotly_chart(fig_bar)

        fig_pie = px.pie(data_frame=year_2018_fake, names='Subject', width=600, height=500, hole=0.4, title='<b>FIG 3.2: Donut Chart of Types of Politics of Fake News</b>',
                         color_discrete_sequence=px.colors.sequential.RdBu,)
        fig_pie.update_traces(textfont_size=16,)
        fig_pie.update_layout(
            title_x=0.5,)
        st.plotly_chart(fig_pie)

        fig_scatter = px.scatter(data_frame=year_2018_fake, x='Author', color='Author', labels={
            "Author": "<b>Author</b>",
            "index": "<b>Count of Max News provided by Author</b>"
        }, title="<b>FIG 4.2: Scatter Graph of Author which provided Fake News</b>", height=500, width=600)
        fig_scatter.update_layout(
            title_x=0.5,
            xaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            yaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            plot_bgcolor='rgb(243, 243, 243)',
        )
        st.plotly_chart(fig_scatter)

        fig_area = px.bar(year_2018_fake, y="Location",  labels={
            "Location": "<b>Location</b>",
                          "count": "<b>Count of News at specific Location</b>",
                          }, title="<b>FIG 5.2: Bar Chart of Fake News at Specific Location<b>", height=500, width=600, color_discrete_sequence=px.colors.qualitative.Alphabet)
        fig_area.update_layout(
            title_x=0.5,
            xaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            yaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            plot_bgcolor='rgb(243, 243, 243)',
        )
        st.plotly_chart(fig_area)

elif (selected == '2019'):
    
    Re['date'] = pd.to_datetime(Re['Published_ Date'], format='%Y-%m-%d')
    year_2019_Real= Re.loc[(Re['date'] >= '2019-01-01')
                   & (Re['date'] <= '2019-12-31')]
   
    with column1:
        fig_p = px.pie(data_frame=year_2019_Real, names='Party_Affiliation', width=600, height=500, title='<b>FIG 1.1: Pie Chart of Party Related to Real News</b>',
                       color_discrete_sequence=px.colors.qualitative.Alphabet)
        fig_p.update_layout(title_x=0.5, )
        fig_p.update_traces(textfont_size=16,)
        st.plotly_chart(fig_p)

        fig_bar = px.bar(data_frame=year_2019_Real, y='Source', labels={'count': "<b>Count of News(1 box=1 Unit)</b>", "Source": "<b>Channels</b>"},
                         color_discrete_sequence=px.colors.qualitative.Dark2,height=500, width=600, title='<b>FIG 2.1:Bar Chart of Channels which provided Real News</b>', color='Source')
        fig_bar.update_layout(
            title_x=0.5,
            xaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            yaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
           
        )
        st.plotly_chart(fig_bar)

        fig_pie = px.pie(data_frame=year_2019_Real, names='Subject', width=600, height=500, hole=0.4, title='<b>FIG 3.1: Donut Chart of Types of Politics of Real News</b>',
                         color_discrete_sequence=px.colors.sequential.algae_r,)
        fig_pie.update_traces(textfont_size=16,)
        fig_pie.update_layout(
            title_x=0.5,)
        st.plotly_chart(fig_pie)

        fig_scatter = px.scatter(data_frame=year_2019_Real, x='Author', color='Author', labels={
            "Author": "<b>Author</b>",
            "index": "<b>Count of Max News provided by Author</b>"
        }, title="<b>FIG 4.1: Scatter Graph of Author which provided Real News</b>", height=500, width=600)
        fig_scatter.update_layout(
            title_x=0.5,
            xaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            yaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            plot_bgcolor='rgb(243, 243, 243)',
        )
        st.plotly_chart(fig_scatter)

        fig_area = px.bar(year_2019_Real, y="Location",  labels={
            "Location": "<b>Location</b>",
                          "count": "<b>Count of News at specific Location</b>",
                          }, title="<b>FIG 5.1: Bar Chart of Real News at Specific Location<b>", height=500, width=600, color_discrete_sequence=px.colors.sequential.Blackbody)
        fig_area.update_layout(
            title_x=0.5,
            xaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            yaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            plot_bgcolor='rgb(243, 243, 243)',
        )
        st.plotly_chart(fig_area)

    with column2:
        df['date'] = pd.to_datetime(df['Published_ Date'], format='%d-%m-%Y')
        year_2019_fake = df.loc[(df['date'] >= '01-01-2019')
                   & (df['date'] <= '31-12-2019')]
        fig_p = px.pie(data_frame=year_2019_fake, names='Party_Affiliation', width=600, height=500, title='<b>FIG 1.2: Pie Chart of Party Related to Fake News</b>',
                       color_discrete_sequence=px.colors.qualitative.Pastel)
        fig_p.update_layout(title_x=0.5, )
        fig_p.update_traces(textfont_size=16,)
        st.plotly_chart(fig_p)

        fig_bar = px.bar(data_frame=year_2019_fake, y='Source', labels={'count': "<b>Count of News(1 box=1 Unit)</b>", "Source": "<b>Channels</b>"},
                         height=500, width=600, title='<b>FIG 2.2: Bar Chart of Channels which provided Fake News</b>', color_discrete_sequence=px.colors.qualitative.Light24_r)
        fig_bar.update_layout(
            title_x=0.5,
            xaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            yaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            plot_bgcolor='rgb(243, 243, 243)',
        )
        st.plotly_chart(fig_bar)

        fig_pie = px.pie(data_frame=year_2019_fake, names='Subject', width=600, height=500, hole=0.4, title='<b>FIG 3.2: Donut Chart of Types of Politics of Fake News</b>',
                         color_discrete_sequence=px.colors.sequential.Bluered,)
        fig_pie.update_traces(textfont_size=16,)
        fig_pie.update_layout(
            title_x=0.5,)
        st.plotly_chart(fig_pie)

        fig_scatter = px.scatter(data_frame=year_2019_fake, x='Author', color='Author', labels={
            "Author": "<b>Author</b>",
            "index": "<b>Count of Max News provided by Author</b>"
        }, title="<b>FIG 4.2: Scatter Graph of Author which provided Fake News</b>", height=500, width=600)
        fig_scatter.update_layout(
            title_x=0.5,
            xaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            yaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            plot_bgcolor='rgb(243, 243, 243)',
        )
        st.plotly_chart(fig_scatter)

        fig_area = px.bar(year_2019_fake, y="Location",  labels={
            "Location": "<b>Location</b>",
                          "count": "<b>Count of News at specific Location</b>",
                          }, title="<b>FIG 5.2: Bar Chart of Fake News at Specific Location<b>", height=500, width=600, color_discrete_sequence=px.colors.qualitative.Dark24)
        fig_area.update_layout(
            title_x=0.5,
            xaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            yaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            plot_bgcolor='rgb(243, 243, 243)',
        )
        st.plotly_chart(fig_area)
elif(selected=='2020'):
    Re['date'] = pd.to_datetime(Re['Published_ Date'], format='%Y-%m-%d')
    year_2020_Real= Re.loc[(Re['date'] >= '2020-01-01')
                   & (Re['date'] <= '2020-12-31')]
   
    with column1:
        fig_p = px.pie(data_frame=year_2020_Real, names='Party_Affiliation', width=600, height=500, title='<b>FIG 1.1: Pie Chart of Party Related to Real News</b>',
                       color_discrete_sequence=px.colors.qualitative.Prism)
        fig_p.update_layout(title_x=0.5, )
        fig_p.update_traces(textfont_size=16,)
        st.plotly_chart(fig_p)

        fig_bar = px.bar(data_frame=year_2020_Real, y='Source', labels={'count': "<b>Count of News(1 box=1 Unit)</b>", "Source": "<b>Channels</b>"},
                         color='Source',height=500, width=600, title='<b>FIG 2.1:Bar Chart of Channels which provided Real News</b>', )
        fig_bar.update_layout(
            title_x=0.5,
            xaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            yaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
           
        )
        st.plotly_chart(fig_bar)

        fig_pie = px.pie(data_frame=year_2020_Real, names='Subject', width=600, height=500, hole=0.4, title='<b>FIG 3.3: Donut Chart of Types of Politics of Real News</b>',
                         color_discrete_sequence=px.colors.sequential.Burg,)
        fig_pie.update_traces(textfont_size=16,)
        fig_pie.update_layout(
            title_x=0.5,)
        st.plotly_chart(fig_pie)

        fig_scatter = px.scatter(data_frame=year_2020_Real, x='Author', color='Author', labels={
            "Author": "<b>Author</b>",
            "index": "<b>Count of Max News provided by Author</b>"
        }, title="<b>FIG 4.1: Scatter Graph of Author which provided Real News</b>", height=500, width=600)
        fig_scatter.update_layout(
            title_x=0.5,
            xaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            yaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            plot_bgcolor='rgb(243, 243, 243)',
        )
        st.plotly_chart(fig_scatter)

        fig_area = px.bar(year_2020_Real, y="Location",  labels={
            "Location": "<b>Location</b>",
                          "count": "<b>Count of News at specific Location</b>",
                          }, title="<b>FIG 5.1: Bar Chart of Real News at Specific Location<b>", height=500, width=600, color_discrete_sequence=px.colors.sequential.Cividis)
        fig_area.update_layout(
            title_x=0.5,
            xaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            yaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            plot_bgcolor='rgb(243, 243, 243)',
        )
        st.plotly_chart(fig_area)

    with column2:
        df['date'] = pd.to_datetime(df['Published_ Date'], format='%d-%m-%Y')
        year_2020_fake = df.loc[(df['date'] >= '01-01-2020')
                   & (df['date'] <= '31-12-2020')]
        
        fig_p = px.pie(data_frame=year_2020_fake, names='Party_Affiliation', width=600, height=500, title='<b>FIG 1.2: Pie Chart of Party Related to Fake News</b>',
                       color_discrete_sequence=px.colors.qualitative.G10_r)
        fig_p.update_layout(title_x=0.5, )
        fig_p.update_traces(textfont_size=16,)
        st.plotly_chart(fig_p)

        fig_bar = px.bar(data_frame=year_2020_fake, y='Source', labels={'count': "<b>Count of News(1 box=1 Unit)</b>", "Source": "<b>Channels</b>"},
                         height=500, width=600, title='<b>FIG 2.2: Bar Chart of Channels which provided Fake News</b>', color='Source')
        fig_bar.update_layout(
            title_x=0.5,
            xaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            yaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            plot_bgcolor='rgb(243, 243, 243)',
        )
        st.plotly_chart(fig_bar)

        fig_pie = px.pie(data_frame=year_2020_fake, names='Subject', width=600, height=500, hole=0.4, title='<b>FIG 3.2: Donut Chart of Types of Politics of Fake News</b>',
                         color_discrete_sequence=px.colors.sequential.Electric_r,)
        fig_pie.update_traces(textfont_size=16,)
        fig_pie.update_layout(
            title_x=0.5,)
        st.plotly_chart(fig_pie)

        fig_scatter = px.scatter(data_frame=year_2020_fake, x='Author', color='Author', labels={
            "Author": "<b>Author</b>",
            "index": "<b>Count of Max News provided by Author</b>"
        }, title="<b>FIG 4.2: Scatter Graph of Author which provided Fake News</b>", height=500, width=600)
        fig_scatter.update_layout(
            title_x=0.5,
            xaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            yaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            plot_bgcolor='rgb(243, 243, 243)',
        )
        st.plotly_chart(fig_scatter)

        fig_area = px.bar(year_2020_fake, y="Location",  labels={
            "Location": "<b>Location</b>",
                          "count": "<b>Count of News at specific Location</b>",
                          }, title="<b>FIG 5.2: Bar Chart of Fake News at Specific Location<b>", height=500, width=600, color_discrete_sequence=px.colors.qualitative.Dark24)
        fig_area.update_layout(
            title_x=0.5,
            xaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            yaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            plot_bgcolor='rgb(243, 243, 243)',
        )
        st.plotly_chart(fig_area)
elif(selected=='2021'):
    Re['date'] = pd.to_datetime(Re['Published_ Date'], format='%Y-%m-%d')
    year_2021_Real= Re.loc[(Re['date'] >= '2021-01-01')
                   & (Re['date'] <= '2021-12-31')]
   
    with column1:
        fig_p = px.pie(data_frame=year_2021_Real, names='Party_Affiliation', width=600, height=500, title='<b>FIG 1.1: Pie Chart of Party Related to Real News</b>',
                       color_discrete_sequence=px.colors.qualitative.Antique)
        fig_p.update_layout(title_x=0.5, )
        fig_p.update_traces(textfont_size=16,)
        st.plotly_chart(fig_p)

        fig_bar = px.bar(data_frame=year_2021_Real, y='Source', labels={'count': "<b>Count of News(1 box=1 Unit)</b>", "Source": "<b>Channels</b>"},
                       height=500,color='Source', width=600, title='<b>FIG 2.1:Bar Chart of Channels which provided Real News</b>', color_discrete_sequence=px.colors.qualitative.Bold_r )
        fig_bar.update_layout(
            title_x=0.5,
            xaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            yaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
           
        )
        st.plotly_chart(fig_bar)

        fig_pie = px.pie(data_frame=year_2021_Real, names='Subject', width=600, height=500, hole=0.4, title='<b>FIG 3.1: Donut Chart of Types of Politics of Real News</b>',
                         color_discrete_sequence=px.colors.sequential.Mint,)
        fig_pie.update_traces(textfont_size=16,)
        fig_pie.update_layout(
            title_x=0.5,)
        st.plotly_chart(fig_pie)

        fig_scatter = px.scatter(data_frame=year_2021_Real, x='Author', color='Author', labels={
            "Author": "<b>Author</b>",
            "index": "<b>Count of Max News provided by Author</b>"
        }, title="<b>FIG 4.1: Scatter Graph of Author which provided Real News</b>", height=500, width=600)
        fig_scatter.update_layout(
            title_x=0.5,
            xaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            yaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            plot_bgcolor='rgb(243, 243, 243)',
        )
        st.plotly_chart(fig_scatter)

        fig_area = px.bar(year_2021_Real, y="Location",  labels={
            "Location": "<b>Location</b>",
                          "count": "<b>Count of News at specific Location</b>",
                          }, title="<b>FIG 5.1: Bar Chart of Real News at Specific Location<b>", height=500, width=600, color_discrete_sequence=px.colors.sequential.Magma)
        fig_area.update_layout(
            title_x=0.5,
            xaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            yaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            plot_bgcolor='rgb(243, 243, 243)',
        )
        st.plotly_chart(fig_area)

    with column2:
        df['date'] = pd.to_datetime(df['Published_ Date'], format='%d-%m-%Y')
        year_2021_fake = df.loc[(df['date'] >= '01-01-2021')
                   & (df['date'] <= '31-12-2021')]
        fig_p = px.pie(data_frame=year_2021_fake, names='Party_Affiliation', width=600, height=500, title='<b>FIG 1.2: Pie Chart of Party Related to Fake News</b>',
                       color_discrete_sequence=px.colors.qualitative.Set1)
        fig_p.update_layout(title_x=0.5, )
        fig_p.update_traces(textfont_size=16,)
        st.plotly_chart(fig_p)

        fig_bar = px.bar(data_frame=year_2021_fake, y='Source', labels={'count': "<b>Count of News(1 box=1 Unit)</b>", "Source": "<b>Channels</b>"},
                         height=500, width=600, title='<b>FIG 2.2: Bar Chart of Channels which provided Fake News</b>', color='Source')
        fig_bar.update_layout(
            title_x=0.5,
            xaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            yaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            plot_bgcolor='rgb(243, 243, 243)',
        )
        st.plotly_chart(fig_bar)

        fig_pie = px.pie(data_frame=year_2021_fake, names='Subject', width=600, height=500, hole=0.4, title='<b>FIG 3.2: Donut Chart of Types of Politics of Fake News</b>',
                         color_discrete_sequence=px.colors.sequential.OrRd,)
        fig_pie.update_traces(textfont_size=16,)
        fig_pie.update_layout(
            title_x=0.5,)
        st.plotly_chart(fig_pie)

        fig_scatter = px.scatter(data_frame=year_2021_fake, x='Author', color='Author', labels={
            "Author": "<b>Author</b>",
            "index": "<b>Count of Max News provided by Author</b>"
        }, title="<b>FIG 4.2: Scatter Graph of Author which provided Fake News</b>", height=500, width=600)
        fig_scatter.update_layout(
            title_x=0.5,
            xaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            yaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            plot_bgcolor='rgb(243, 243, 243)',
        )
        st.plotly_chart(fig_scatter)

        fig_area = px.bar(year_2021_fake, y="Location",  labels={
            "Location": "<b>Location</b>",
                          "count": "<b>Count of News at specific Location</b>",
                          }, title="<b>FIG 5.2: Bar Chart of Fake News at Specific Location<b>", height=500, width=600, color_discrete_sequence=px.colors.qualitative.Vivid_r)
        fig_area.update_layout(
            title_x=0.5,
            xaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            yaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            plot_bgcolor='rgb(243, 243, 243)',
        )
        st.plotly_chart(fig_area)
elif(selected=='2022'):
    Re['date'] = pd.to_datetime(Re['Published_ Date'], format='%d-%m-%Y')
    year_2022_Real= Re.loc[(Re['date'] >= '01-01-2022')
                   & (Re['date'] <= '31-12-2022')]
   
    with column1:
        fig_p = px.pie(data_frame=year_2022_Real, names='Party_Affiliation', width=600, height=500, title='<b>FIG 1.1: Pie Chart of Party Related to Real News</b>',
                       color_discrete_sequence=px.colors.qualitative.Set3_r)
        fig_p.update_layout(title_x=0.5, )
        fig_p.update_traces(textfont_size=16,)
        st.plotly_chart(fig_p)

        fig_bar = px.bar(data_frame=year_2022_Real, y='Source', labels={'count': "<b>Count of News(1 box=1 Unit)</b>", "Source": "<b>Channels</b>"},
                         color_discrete_sequence=px.colors.qualitative.D3,height=500, width=600, title='<b>FIG 2.1:Bar Chart of Channels which provided Real News</b>', color='Source')
        fig_bar.update_layout(
            title_x=0.5,
            xaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            yaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
           
        )
        st.plotly_chart(fig_bar)

        fig_pie = px.pie(data_frame=year_2022_Real, names='Subject', width=600, height=500, hole=0.4, title='<b>FIG 3.1: Donut Chart of Types of Politics of Real News</b>',
                         color_discrete_sequence=px.colors.sequential.ice,)
        fig_pie.update_traces(textfont_size=16,)
        fig_pie.update_layout(
            title_x=0.5,)
        st.plotly_chart(fig_pie)

        fig_scatter = px.scatter(data_frame=year_2022_Real, x='Author', color='Author', labels={
            "Author": "<b>Author</b>",
            "index": "<b>Count of Max News provided by Author</b>"
        }, title="<b>FIG 4.1: Scatter Graph of Author which provided Real News</b>", height=500, width=600)
        fig_scatter.update_layout(
            title_x=0.5,
            xaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            yaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            plot_bgcolor='rgb(243, 243, 243)',
        )
        st.plotly_chart(fig_scatter)

        fig_area = px.bar(year_2022_Real, y="Location",  labels={
            "Location": "<b>Location</b>",
                          "count": "<b>Count of News at specific Location</b>",
                          }, title="<b>FIG 5.1: Bar Chart of Real News at Specific Location<b>", height=500, width=600, color_discrete_sequence=px.colors.sequential.Brwnyl_r)
        fig_area.update_layout(
            title_x=0.5,
            xaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            yaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            plot_bgcolor='rgb(243, 243, 243)',
        )
        st.plotly_chart(fig_area)

    with column2:
        df['date'] = pd.to_datetime(df['Published_ Date'], format='%d-%m-%Y')
        year_2022_fake = df.loc[(df['date'] >= '01-01-2022')
                   & (df['date'] <= '31-12-2022')]
        fig_p = px.pie(data_frame=year_2022_fake, names='Party_Affiliation', width=600, height=500, title='<b>FIG 1.2: Pie Chart of Party Related to Fake News</b>',
                       color_discrete_sequence=px.colors.qualitative.T10_r)
        fig_p.update_layout(title_x=0.5, )
        fig_p.update_traces(textfont_size=16,)
        st.plotly_chart(fig_p)

        fig_bar = px.bar(data_frame=year_2022_fake, y='Source', labels={'count': "<b>Count of News(1 box=1 Unit)</b>", "Source": "<b>Channels</b>"},
                         height=500, width=600, title='<b>FIG 2.2: Bar Chart of Channels which provided Fake News</b>', color='Source')
        fig_bar.update_layout(
            title_x=0.5,
            xaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            yaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            plot_bgcolor='rgb(243, 243, 243)',
        )
        st.plotly_chart(fig_bar)

        fig_pie = px.pie(data_frame=year_2022_fake, names='Subject', width=600, height=500, hole=0.4, title='<b>FIG 3.2: Donut Chart of Types of Politics of Fake News</b>',
                         color_discrete_sequence=px.colors.sequential.Darkmint,)
        fig_pie.update_traces(textfont_size=16,)
        fig_pie.update_layout(
            title_x=0.5,)
        st.plotly_chart(fig_pie)

        fig_scatter = px.scatter(data_frame=year_2022_fake, x='Author', color='Author', labels={
            "Author": "<b>Author</b>",
            "index": "<b>Count of Max News provided by Author</b>"
        }, title="<b>FIG 4.2: Scatter Graph of Author which provided Fake News</b>", height=500, width=600)
        fig_scatter.update_layout(
            title_x=0.5,
            xaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            yaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            plot_bgcolor='rgb(243, 243, 243)',
        )
        st.plotly_chart(fig_scatter)

        fig_area = px.bar(year_2022_fake, y="Location",  labels={
            "Location": "<b>Location</b>",
                          "count": "<b>Count of News at specific Location</b>",
                          }, title="<b>FIG 5.2: Bar Chart of Fake News at Specific Location<b>", height=500, width=600, color_discrete_sequence=px.colors.qualitative.Alphabet)
        fig_area.update_layout(
            title_x=0.5,
            xaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            yaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            plot_bgcolor='rgb(243, 243, 243)',
        )
        st.plotly_chart(fig_area)
elif (selected == '2023'):
    
    Re['date'] = pd.to_datetime(Re['Published_ Date'], format='%Y-%m-%d')
    year_2019_Real= Re.loc[(Re['date'] >= '2023-01-01')
                   & (Re['date'] <= '2023-12-31')]
   
    with column1:
        fig_p = px.pie(data_frame=year_2019_Real, names='Party_Affiliation', width=600, height=500, title='<b>FIG 1.1: Pie Chart of Party Related to Real News</b>',
                       color_discrete_sequence=px.colors.qualitative.Plotly)
        fig_p.update_layout(title_x=0.5, )
        fig_p.update_traces(textfont_size=16,)
        st.plotly_chart(fig_p)

        fig_bar = px.bar(data_frame=year_2019_Real, y='Source', labels={'count': "<b>Count of News(1 box=1 Unit)</b>", "Source": "<b>Channels</b>"},
                         color_discrete_sequence=px.colors.qualitative.Pastel,height=500, width=600, title='<b>FIG 2.1:Bar Chart of Channels which provided Real News</b>', color='Source')
        fig_bar.update_layout(
            title_x=0.5,
            xaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            yaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
           
        )
        st.plotly_chart(fig_bar)

        fig_pie = px.pie(data_frame=year_2019_Real, names='Subject', width=600, height=500, hole=0.4, title='<b>FIG 3.1: Donut Chart of Types of Politics of Real News</b>',
                         color_discrete_sequence=px.colors.sequential.Cividis_r,)
        fig_pie.update_traces(textfont_size=16,)
        fig_pie.update_layout(
            title_x=0.5,)
        st.plotly_chart(fig_pie)

        fig_scatter = px.scatter(data_frame=year_2019_Real, x='Author', color='Author', labels={
            "Author": "<b>Author</b>",
            "index": "<b>Count of Max News provided by Author</b>"
        }, title="<b>FIG 4.1: Scatter Graph of Author which provided Real News</b>", height=500, width=600)
        fig_scatter.update_layout(
            title_x=0.5,
            xaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            yaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            plot_bgcolor='rgb(243, 243, 243)',
        )
        st.plotly_chart(fig_scatter)

        fig_area = px.bar(year_2019_Real, y="Location",  labels={
            "Location": "<b>Location</b>",
                          "count": "<b>Count of News at specific Location</b>",
                          }, title="<b>FIG 5.1: Bar Chart of Real News at Specific Location<b>", height=500, width=600, color_discrete_sequence=px.colors.sequential.Electric_r)
        fig_area.update_layout(
            title_x=0.5,
            xaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            yaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            plot_bgcolor='rgb(243, 243, 243)',
        )
        st.plotly_chart(fig_area)

    with column2:
        df['date'] = pd.to_datetime(df['Published_ Date'], format='%d-%m-%Y')
        year_2019_fake = df.loc[(df['date'] >= '01-01-2023')
                   & (df['date'] <= '31-12-2023')]
        fig_p = px.pie(data_frame=year_2019_fake, names='Party_Affiliation', width=600, height=500, title='<b>FIG 1.2: Pie Chart of Party Related to Fake News</b>',
                       color_discrete_sequence=px.colors.qualitative.Set3_r)
        fig_p.update_layout(title_x=0.5, )
        fig_p.update_traces(textfont_size=16,)
        st.plotly_chart(fig_p)

        fig_bar = px.bar(data_frame=year_2019_fake, y='Source', labels={'count': "<b>Count of News(1 box=1 Unit)</b>", "Source": "<b>Channels</b>"},
                         height=500, width=600, title='<b>FIG 2.2: Bar Chart of Channels which provided Fake News</b>', color_discrete_sequence=px.colors.qualitative.Vivid_r)
        fig_bar.update_layout(
            title_x=0.5,
            xaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            yaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            plot_bgcolor='rgb(243, 243, 243)',
        )
        st.plotly_chart(fig_bar)

        fig_pie = px.pie(data_frame=year_2019_fake, names='Subject', width=600, height=500, hole=0.4, title='<b>FIG 3.2: Donut Chart of Types of Politics of Fake News</b>',
                         color_discrete_sequence=px.colors.sequential.Aggrnyl,)
        fig_pie.update_traces(textfont_size=16,)
        fig_pie.update_layout(
            title_x=0.5,)
        st.plotly_chart(fig_pie)

        fig_scatter = px.scatter(data_frame=year_2019_fake, x='Author', color='Author', labels={
            "Author": "<b>Author</b>",
            "index": "<b>Count of Max News provided by Author</b>"
        }, title="<b>FIG 4.2: Scatter Graph of Author which provided Fake News</b>", height=500, width=600)
        fig_scatter.update_layout(
            title_x=0.5,
            xaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            yaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            plot_bgcolor='rgb(243, 243, 243)',
        )
        st.plotly_chart(fig_scatter)

        fig_area = px.bar(year_2019_fake, y="Location",  labels={
            "Location": "<b>Location</b>",
                          "count": "<b>Count of News at specific Location</b>",
                          }, title="<b>FIG 5.2: Bar Chart of Fake News at Specific Location<b>", height=500, width=600, color_discrete_sequence=px.colors.qualitative.T10_r)
        fig_area.update_layout(
            title_x=0.5,
            xaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            yaxis=dict(

                gridcolor='white',
                gridwidth=3,
            ),
            plot_bgcolor='rgb(243, 243, 243)',
        )
        st.plotly_chart(fig_area)
else:

    st.markdown('KEY METRICS')
    c1, c2, c3, c4= st.columns(4)
    c1.metric(label="TOTAL NEWS", value='5K')
    c2.metric("REAL NEWS", "4K", "0.80%")
    c3.metric("FAKE NEWS", "1K", "0.20%")
    c4.metric("ENSEMBLE", "91.85%")
    cc1, cc2, cc3 = st.columns(3)
    with cc1:
        Re['date_year'] = pd.to_datetime(Re['Published_ Date'], format='%Y-%m-%d')
        Re['Year']=Re['date_year'].dt.year
        news_by_year = Re.groupby("Year").count()["Label"]
       
        fig_line = px.line(data_frame=news_by_year, x=news_by_year.index, y=news_by_year.values, height=400,
                           width=420,orientation='v',color_discrete_sequence=['green'],title="<b>Real News of Last 5 Years</b>",
                           labels={"x": "<b>Years</b>", "y": "<b>Count of Year(Maximum Real News Published)</b>"},
                           )
        fig_line.update_xaxes(title_text="<b>Years</b>"  )
        fig_line.update_layout(
            title_x=0.5,
            xaxis=dict(

                gridcolor='white',
                gridwidth=2,
            ),
            yaxis=dict(

                gridcolor='white',
                gridwidth=2,
            ),
            plot_bgcolor='rgb(255, 255, 255)',
        )
        st.plotly_chart(fig_line)

    with cc2:
        df['date_year'] = pd.to_datetime(df['Published_ Date'], format='%d-%m-%Y')
        df['Year']=df['date_year'].dt.year
        news_by_year = df.groupby("Year").count()["Label"]
       
        fig_line = px.line(data_frame=news_by_year, x=news_by_year.index, y=news_by_year.values,height=400,
                           width=420,
                           labels={"x": "<b>Years</b>", "y": "<b>Count of Year(Maximum Fake News Published)</b>"},
                             title="<b>Fake News of Last 5 Years</b>",color_discrete_sequence=['red'])
        fig_line.update_xaxes(title_text="<b>Years</b>"  )
        fig_line.update_layout(
            title_x=0.5,
            xaxis=dict(

                gridcolor='white',
                gridwidth=2,
            ),
            yaxis=dict(

                gridcolor='white',

                gridwidth=2,
            ),
            plot_bgcolor='rgb(255, 255, 255)',
        )
        st.plotly_chart(fig_line)

    with cc3:
        
        fig_p = px.pie(data_frame=df_combine, names='Label', width=400, height=400, title='<b>Pie Chart of Fake and Real News</b>',
                       color_discrete_sequence=px.colors.qualitative.Plotly_r)
        
        fig_p.update_layout(title_x=0.5, )
        fig_p.update_traces(textfont_size=16,)
        st.plotly_chart(fig_p)
