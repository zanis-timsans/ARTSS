# -*- coding: utf-8 -*-

# visit http://127.0.0.1:8050/ in your web browser.

# Load libraries
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from dash.dependencies import Input, Output

# Styles - CERULEAN (!), COSMO, CYBORG, DARKLY, FLATLY, JOURNAL, LITERA, LUMEN, LUX, MATERIA (!),
# MINTY, PULSE (!), SANDSTONE (!), SIMPLEX, SKETCHY, SLATE, SOLAR, SPACELAB (!), SUPERHERO, UNITED (!), YETI (!)
external_stylesheets = [dbc.themes.PULSE]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets,  # , external_stylesheets=external_stylesheets
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'}]
                )
server = app.server

# PREPROCESSING Load dataframe
camera = dict(
    eye=dict(x=2, y=2, z=0.8)
)


# Create dataframe for visualising 'Complete learning acquisition landscape'
df_tele = pd.DataFrame(data=[['too complicated content', 0.222, 0.111, 0.666],
                             ['too easy content', 0, 1, 0, ],
                             ['ideally matching content', 0.667, 0.333, 0]],
                       columns=['content', 'N-P', 'P-P', 'X-N'], index=None)

fig = go.Figure(data=[
    go.Mesh3d(
        x=df_tele['N-P'],
        y=df_tele['P-P'],
        z=df_tele['X-N'],
        color='steelblue',
        opacity=0.3,
        hoverinfo='skip',
    )
])

fig.update_layout(
    template='plotly',
    scene_camera=camera,
    scene=dict(
        xaxis_title="Piemērots",
        yaxis_title="Viegls",
        zaxis_title="Nepiemērots",
        xaxis=dict(
            nticks=6, range=[0, 1],
            backgroundcolor="rgb(200, 200, 230)",
            gridcolor="white",
            showbackground=True,
            zerolinecolor="white",
            showspikes=False),
        yaxis=dict(
            nticks=6, range=[0, 1],
            backgroundcolor="rgb(230, 200,230)",
            gridcolor="white",
            showbackground=True,
            zerolinecolor="white",
            showspikes=False),
        zaxis=dict(
            nticks=6, range=[0, 1],
            backgroundcolor="rgb(230, 230,200)",
            gridcolor="white",
            showbackground=True,
            zerolinecolor="white",
            showspikes=False),
    ),
    height=600,
    margin=dict(
        r=0, l=0,
        b=0, t=0),
)

# APPLICATION LAYOUT
app.layout = html.Div([
    dbc.Row(dbc.Col([
        html.H1('ARTSS datu vizualizācija', className="text-center my-5"),
        html.Div('''
                Šajā tīmekļa lietotnē skolotājs var vizuāli novērot kursa satura piemērotību un efektivitāti 
                izmantojot Telecīdas
                ''', className="text-center my-5"),
    ], width=8,
    ), justify='center',
    ),

    dbc.Row([
        dbc.Col([
            html.Div([html.H5('Diagramma'),
                      '''
                Vizualizācijas metodes nosaukums ir Telecīdas. Tā ir 3D diagramma, kur katrs punkts plaknē norāda uz 
                vienu no satura tēmām. Apmācamajam atbilstošs un efektīvs saturs ir tad, kad punkts atrodas tuvāk  
                N-P=0.6.
                '''], className='ml-3 my-3 border p-3'
                     ),
            html.Div("Izvēlies kursu", className='ml-3'),
            dcc.Dropdown(options=[
                {'label': 'Fizika 8. klasei',
                 'value': 'https://artss.mii.lv/webservice/rest/server.php?courseid=17&wstoken'
                          '=a78e76c2570f41a3f180d0979914c7dc&wsfunction'
                          '=local_notifyemailsignup_functiongetstudentactivitydata&moodlewsrestformat=json',
                 'disabled': True},
                {'label': 'Fizika 9. klasei',
                 'value': 'https://artss.mii.lv/webservice/rest/server.php?courseid=18&wstoken'
                          '=a78e76c2570f41a3f180d0979914c7dc&wsfunction'
                          '=local_notifyemailsignup_functiongetstudentactivitydata&moodlewsrestformat=json'},
                {'label': 'Fizika 10. klasei',
                 'value': 'https://artss.mii.lv/webservice/rest/server.php?courseid=19&wstoken'
                          '=a78e76c2570f41a3f180d0979914c7dc&wsfunction'
                          '=local_notifyemailsignup_functiongetstudentactivitydata&moodlewsrestformat=json'},
                {'label': 'Medijpratība',
                 'value': 'https://artss.mii.lv/webservice/rest/server.php?courseid=14&wstoken'
                          '=a78e76c2570f41a3f180d0979914c7dc&wsfunction'
                          '=local_notifyemailsignup_functiongetstudentactivitydata&moodlewsrestformat=json'},
                {'label': 'Study Design and Implementation',
                 'value': 'https://artss.mii.lv/webservice/rest/server.php?courseid=15&wstoken'
                          '=a78e76c2570f41a3f180d0979914c7dc&wsfunction'
                          '=local_notifyemailsignup_functiongetstudentactivitydata&moodlewsrestformat=json'},
                {'label': 'Datorika un informātika',
                 'value': 'https://artss.mii.lv/webservice/rest/server.php?courseid=12&wstoken'
                          '=a78e76c2570f41a3f180d0979914c7dc&wsfunction'
                          '=local_notifyemailsignup_functiongetstudentactivitydata&moodlewsrestformat=json',
                 'disabled': True},
                {'label': 'Digitālās prasmes 7.-12. klašu latviešu valodas skolotājiem',
                 'value': 'https://artss.mii.lv/webservice/rest/server.php?courseid=11&wstoken'
                          '=a78e76c2570f41a3f180d0979914c7dc&wsfunction'
                          '=local_notifyemailsignup_functiongetstudentactivitydata&moodlewsrestformat=json',
                 'disabled': True},
                {'label': 'Ievads programmēšanas valodā Python', 'value':
                    'https://artss.mii.lv/webservice/rest/server.php?courseid=10&wstoken'
                    '=a78e76c2570f41a3f180d0979914c7dc&wsfunction'
                    '=local_notifyemailsignup_functiongetstudentactivitydata&moodlewsrestformat=json',
                 'disabled': True},
                {'label': 'Kiberdrošības pamati iesācējiem',
                 'value': 'https://artss.mii.lv/webservice/rest/server.php?courseid=9&wstoken'
                          '=a78e76c2570f41a3f180d0979914c7dc&wsfunction'
                          '=local_notifyemailsignup_functiongetstudentactivitydata&moodlewsrestformat=json',
                 'disabled': True},
                {'label': 'Komercdarbība',
                 'value': 'https://artss.mii.lv/webservice/rest/server.php?courseid=7&wstoken'
                          '=a78e76c2570f41a3f180d0979914c7dc&wsfunction'
                          '=local_notifyemailsignup_functiongetstudentactivitydata&moodlewsrestformat=json'},
                {'label': 'VR tehnoloģijas',
                 'value': 'https://artss.mii.lv/webservice/rest/server.php?courseid=6&wstoken'
                          '=a78e76c2570f41a3f180d0979914c7dc&wsfunction'
                          '=local_notifyemailsignup_functiongetstudentactivitydata&moodlewsrestformat=json',
                 'disabled': True},
                {'label': 'Visaptverošā kvalitātes vadība',
                 'value': 'https://artss.mii.lv/webservice/rest/server.php?courseid=4&wstoken'
                          '=a78e76c2570f41a3f180d0979914c7dc&wsfunction'
                          '=local_notifyemailsignup_functiongetstudentactivitydata&moodlewsrestformat=json',
                 'disabled': True},
                {'label': 'Statistika inženieriem',
                 'value': 'https://artss.mii.lv/webservice/rest/server.php?courseid=3&wstoken'
                          '=a78e76c2570f41a3f180d0979914c7dc&wsfunction'
                          '=local_notifyemailsignup_functiongetstudentactivitydata&moodlewsrestformat=json',
                 'disabled': True},
                {'label': 'Vizuālā programmēšana ar Scratch',
                 'value': 'https://artss.mii.lv/webservice/rest/server.php?courseid=2&wstoken'
                          '=a78e76c2570f41a3f180d0979914c7dc&wsfunction'
                          '=local_notifyemailsignup_functiongetstudentactivitydata&moodlewsrestformat=json'},
                {'label': 'Āfrika',
                 'value': 'https://bpome.mii.lv/webservice/rest/server.php?wstoken=abc77eef5247b3aa21488df6a394a3d4'
                          '&wsfunction=local_getstudentactivitydata_functiongetstudentactivitydata&date_from=0'}
            ],
                # value='https://artss.mii.lv/webservice/rest/server.php?courseid=18&wstoken'
                #           '=a78e76c2570f41a3f180d0979914c7dc&wsfunction',
                searchable=True,
                placeholder='Izvēlies vai ievadi kursa nosaukumu',
                # style={'width': '80%'},
                persistence=True,
                persistence_type='memory',  # memory-tab refresh, session-tab is closed, local-cookies
                id='courses_dropdown',
                className='ml-3 mb-5'
            ),
            html.Div(
                [
                    html.Div([
                        html.H6('Satura piemērotības zonas'),
                        html.Img(title='paraugs', src='assets/landscape-segments.jpg', width='100%'),
                        dbc.Alert("Atbilstošs saturs", color="success", className='mb-0'),
                        dbc.Alert("Neatbilstošs saturs. Pārāk sarežģīts", color="danger", className='my-1'),
                        dbc.Alert("Daļēji neatbilstošs, pārāk viegls saturs. ", color="primary", className='mt-0'),
                    ], className='mb-3 border p-3'),
                ], className='ml-3'
            )
        ], width=3),
        dbc.Col([
            dbc.CardGroup([
                dbc.Card(
                    dbc.CardBody([
                        html.Div('Tēmas', className="card-title text-center"),
                        html.H1(id='tema', className='text-center clearfix')
                    ]), className=""
                ),
                dbc.Card(
                    dbc.CardBody([
                        html.Div('Studenti', className="card-title text-center"),
                        html.H1(id='number_of_students', className='text-center')
                    ]), className=""
                ),
                dbc.Card(
                    dbc.CardBody([
                        html.Div('Jautājumu pāri', className="card-title text-center"),
                        html.H1(id='pari', className='text-center')
                    ]), className=""
                ),
                dbc.Card(
                    dbc.CardBody([
                        html.Div('Analizētie pāri', className="card-title text-center"),
                        html.H1(id='summa', className='text-center clearfix')
                    ]), className=""
                )
            ], className='mt-3 mb-3', style={'columnCount': 2}),
            dbc.Col([
                dcc.Loading(id="loading-2", children=[
                    html.Div(id="loading-output-2", style={'display': 'none'}),
                    dcc.Tabs([
                        dcc.Tab(label='Tēmas', children=[
                            dcc.Graph(
                                id='telecides-unit',
                                figure=fig,
                                config={'displaylogo': False, 'showTips': True},
                            )
                        ]),
                        dcc.Tab(label='Apakštēmas', children=[
                            dcc.Graph(
                                id='telecides-sub-unit',
                                figure=fig,
                                config={'displaylogo': False, 'showTips': True},
                            )
                        ]),
                        dcc.Tab(label='Studenti', children=[
                            dcc.Graph(
                                id='telecides-student',
                                figure=fig,
                                config={'displaylogo': False, 'showTips': True},
                            )
                        ]),
                    ]),
                ], type="default", fullscreen=False),




                # html.H5('Tēmas', className='ac'),
                # dcc.Loading(id="loading-2", children=[
                #     html.Div(id="loading-output-2", style={'display': 'none'}),
                #     dcc.Graph(
                #         # id='telecides-unit',
                #         figure=fig,
                #         config={'displaylogo': False, 'showTips': True},
                #     )], type="default", fullscreen=False),
                # html.H5('Apakštēmas'),
                # dcc.Graph(
                #     # id='telecides-sub-unit',
                #     figure=fig,
                #     config={'displaylogo': False, 'showTips': True},
                # ),
                # html.H5('Studenti', className=''),
                # dcc.Graph(
                #     # id='telecides-student',
                #     figure=fig,
                #     config={'displaylogo': False, 'showTips': True},
                # ),
                # html.H5('Laiks'),
                # dcc.Graph(
                #     id='avg-time',
                #     figure=fig,
                #     config={'displaylogo': False, 'showTips': True},
                # )
            ], className='border'),
        ], width=8),
    ], justify="center"),
    dbc.Row(
        dbc.Col(
            # html.H1('Papildus saturs'),
        ),
        justify='center'
    )
])


# ------------------- CALLBACKS ------------------------------------------------------------------
@app.callback(
    [Output(component_id='telecides-unit', component_property='figure'),
     Output(component_id='telecides-sub-unit', component_property='figure'),
     Output(component_id='telecides-student', component_property='figure'),
     Output(component_id='tema', component_property='children'),
     Output(component_id='number_of_students', component_property='children'),
     Output(component_id='pari', component_property='children'),
     Output(component_id='summa', component_property='children'),
     Output(component_id="loading-output-2", component_property='children')],
    [Input(component_id='courses_dropdown', component_property='value')]
)
def update_telecides(value):
    if value is None:
        # PreventUpdate prevents ALL outputs updating
        raise dash.exceptions.PreventUpdate
    api = value
    df = pd.read_json(api, orient="split")

    df1 = pd.DataFrame(df['user'].values.tolist())
    df1.columns = 'user_' + df1.columns
    col = df.columns.difference(['user'])
    df = pd.concat([df[col], df1], axis=1)

    # Number of unique users including admins and managers
    number_of_users = len(df["user_id"].unique())

    rez = df[df["type"] == "result"]
    # Filter out only first item in 'user_role'

    rez = rez.loc[np.array(list(map(len, rez.user_roles.values))) == 1]

    # Convert column from list to string
    rez['user_roles'] = rez['user_roles'].apply(lambda x: ','.join(map(str, x)))

    # Select only 'student' roles and make copy of original dataframe to avoid slicing view
    rez = rez.loc[rez.user_roles == 'student'].copy()

    # Transform time feature to datetime object
    rez["datetime"] = pd.to_datetime(rez["datetime"])

    # Keeping only first occurrence and dropping all other
    rez = rez.drop_duplicates(subset=['user_id', 'itemid'], keep="first")

    # Drop nevajadzīgās colonas
    rez.drop(['id', 'answer', 'answer_submitted', 'question', 'timestamp', 'type', 'user_roles'], axis=1, inplace=True)

    # Convert everything to uppercase in case there are some in lowercase
    rez['title'] = rez['title'].str.upper()

    # Take last
    rez['letter'] = rez['title'].str.strip().str[-1]

    # Remove rows that are not a or b
    rez = rez[(rez['title'].str.contains('A', case=False)) | (rez['title'].str.contains('B', case=False))].copy()

    # Remove rows with '.' for 'letter' value
    rez = rez[rez['letter'] != '.'].copy()

    # Sakartoti pēc Lietotāja un priekšmeta ID *apskatei*
    rez.sort_values(by=['section', 'lessonid', 'user_id'], inplace=True)

    # mapping true/false to p/n (pareizi/nepareizi)
    di = {'true': 'p', 'false': 'n'}
    rez.replace({'correct_answer': di}, inplace=True)

    # Convert everything to uppercase in case there are some in lowercase
    rez['letter'] = rez['letter'].str.upper()

    a = rez[(rez['letter'].shift(-1) == 'B')].copy()
    b = rez[(rez['letter'] == 'B')].copy()
    ab = a.append(b, sort=True)
    ab.sort_values(by=['section', 'lessonid', 'user_id', 'letter'], inplace=True)
    ab.reset_index(inplace=True)
    ab.drop_duplicates(inplace=True)
    a = ab[(ab['letter'] == 'A')].copy()
    b = ab[(ab['letter'].shift(1) == 'A')].copy()
    ab = a.append(b, sort=True)
    ab.sort_values(by=['section', 'lessonid', 'user_id', 'letter'], inplace=True)
    ab.reset_index(inplace=True)
    ab.drop_duplicates(inplace=True)

    # # All necessary 'A'
    # a = rez[(rez['letter'].shift(-1) == 'B')].copy()
    #
    # # All necessary 'B'
    # b = rez[(rez['letter'] == 'B')].copy()
    #
    # # Combine two filtered dataframes
    # rez = a.append(b, sort=True)
    #
    # # Sort values and reset index
    # rez.sort_values(by=['section', 'lessonid', 'user_id'], inplace=True)
    # rez.reset_index(inplace=True)

    # Number of question pairs
    pari = ab["lessonid"].nunique()

    # Number of students only
    number_of_students = ab["user_id"].nunique()

    # # Join 'p' and 'n' results into one column based on 'a' and 'b' questions. Keep section number. Convert to dataframe
    # # using to_frame
    # final_df = ab.groupby(by=[ab.index // 2, 'section'])['correct_answer'].agg('-'.join).to_frame()
    #
    # # Reset index
    # final_df.reset_index(level=['section'], inplace=True)
    #
    # # Create final dataframe containing sum of all question pairs for each Unit (section)
    # telecides = pd.crosstab(index=final_df['section'], columns=final_df['correct_answer'])
    #
    # # Create necessary column if they do not exist
    # if 'n-n' not in telecides.columns:
    #     telecides['n-n'] = 0
    # if 'n-p' not in telecides.columns:
    #     telecides['n-p'] = 0
    # if 'p-p' not in telecides.columns:
    #     telecides['p-p'] = 0
    # if 'p-n' not in telecides.columns:
    #     telecides['p-n'] = 0
    #
    # # Create column 'x-n' that is sum of 'n-n' and 'p-n' columns
    # telecides['x-n'] = telecides['n-n'] + telecides['p-n']
    # telecides.drop(columns=['n-n', 'p-n'], inplace=True)
    #
    # # Create column sum of all pairs per Unit
    # telecides['sum'] = telecides['n-p'] + telecides['p-p'] + telecides['x-n']
    #
    # # Sum of all question pairs
    # summa = telecides['sum'].sum()
    #
    # # Number of units
    # temas = len(telecides.index)
    #
    # # Create final values using average probability
    # telecides['n-p'] = telecides['n-p'] / telecides['sum']
    # telecides['p-p'] = telecides['p-p'] / telecides['sum']
    # telecides['x-n'] = telecides['x-n'] / telecides['sum']
    # telecides.drop(columns=['sum'], inplace=True)
    #
    # # Create dataframe for visualising 'Complete learning acquisition landscape'
    # df_tele = pd.DataFrame(data=[['too complicated content', 0.222, 0.111, 0.666],
    #                              ['too easy content', 0, 1, 0, ],
    #                              ['ideally matching content', 0.667, 0.333, 0]],
    #                        columns=['content', 'N-P', 'P-P', 'X-N'], index=None)
    # # print(df_tele)
    #
    # fig = go.Figure(data=[
    #     go.Mesh3d(
    #         x=df_tele['N-P'],
    #         y=df_tele['P-P'],
    #         z=df_tele['X-N'],
    #         color='steelblue',
    #         opacity=0.3,
    #         hoverinfo='skip',
    #     ),
    #     go.Scatter3d(
    #         x=telecides['n-p'],
    #         y=telecides['p-p'],
    #         z=telecides['x-n'],
    #         mode="markers",
    #         text=telecides.index,
    #         hovertemplate='Piemērots: %{x:.2f}<br>Viegls: %{y:.2f}<br>Nepiemērots: %{z:.2f}<extra>Tēma: %{text}</extra>',
    #         marker=dict(size=7, symbol="circle", color=telecides)  # color=telecides.index, colorscale='balance'
    #     ),
    # ])
    # fig.update_layout(
    #     template='plotly',
    #     scene_camera=camera,
    #     scene=dict(
    #         xaxis_title="Piemērots",
    #         yaxis_title="Viegls",
    #         zaxis_title="Nepiemērots",
    #         xaxis=dict(
    #             nticks=6, range=[0, 1],
    #             backgroundcolor="rgb(200, 200, 230)",
    #             gridcolor="white",
    #             showbackground=True,
    #             zerolinecolor="white",
    #             showspikes=False),
    #         yaxis=dict(
    #             nticks=6, range=[0, 1],
    #             backgroundcolor="rgb(230, 200,230)",
    #             gridcolor="white",
    #             showbackground=True,
    #             zerolinecolor="white",
    #             showspikes=False),
    #         zaxis=dict(
    #             nticks=6, range=[0, 1],
    #             backgroundcolor="rgb(230, 230,200)",
    #             gridcolor="white",
    #             showbackground=True,
    #             zerolinecolor="white",
    #             showspikes=False),
    #     ),
    #     height=600,
    #     margin=dict(
    #         r=0, l=0,
    #         b=0, t=0),
    # )

    # ---------------------------------------------------------------------------------------

    def final_aggregation(coll, x, y):
        global temas
        global krasa
        global summa
        if coll == 'lessonid':
            content_filter = x['type'].isin(['content'])
            content_df = x[['section', 'lessonid', 'title', 'type']]
            content_df = content_df[content_filter].drop_duplicates(subset=['lessonid']).drop(['type'], axis=1).copy()
            # create dictionary of lesson titles with corresponding lessonid
            lesson_di = pd.Series(content_df.title.values, index=content_df.lessonid).to_dict()
            krasa = 'dodgerblue'

        if coll == 'user_id':
            krasa = 'lightcoral'
        if coll == 'section':
            krasa = 'mediumslateblue'
        # Join 'p' and 'n' results into one column based on 'a' and 'b' questions. Keep lessonid number. Convert to dataframe using to_frame
        x_df = y.groupby(by=[y.index // 2, coll])['correct_answer'].agg('-'.join).to_frame()
        # Reset index
        x_df.reset_index(level=[coll], inplace=True)

        if coll == 'lessonid':
            x_df.replace({'lessonid': lesson_di}, inplace=True)

        # Create final dataframe containing sum of all question pairs for each Unit (section)
        x_df = pd.crosstab(index=x_df[coll], columns=x_df['correct_answer'])

        # Create necessary column if they do not exist
        if 'n-n' not in x_df.columns:
            x_df['n-n'] = 0
        if 'n-p' not in x_df.columns:
            x_df['n-p'] = 0
        if 'p-p' not in x_df.columns:
            x_df['p-p'] = 0
        if 'p-n' not in x_df.columns:
            x_df['p-n'] = 0

        # Create column 'x-n' that is sum of 'n-n' and 'p-n' columns
        x_df['x-n'] = x_df['n-n'] + x_df['p-n']
        x_df.drop(columns=['n-n', 'p-n'], inplace=True)

        # Create column sum of all pairs per Unit
        x_df['sum'] = x_df['n-p'] + x_df['p-p'] + x_df['x-n']

        # Number of units
        if coll == 'section':
            temas = len(x_df.index)

        # Sum of all question pairs
        summa = x_df['sum'].sum()

        # Create final values using average probability
        x_df['n-p'] = x_df['n-p'] / x_df['sum']
        x_df['p-p'] = x_df['p-p'] / x_df['sum']
        x_df['x-n'] = x_df['x-n'] / x_df['sum']
        x_df.drop(columns=['sum'], inplace=True)

        fig = go.Figure(data=[
            go.Mesh3d(
                x=df_tele['N-P'],
                y=df_tele['P-P'],
                z=df_tele['X-N'],
                color='steelblue',
                opacity=0.3,
                hoverinfo='none',
            ),
            go.Scatter3d(
                x=x_df['n-p'],
                y=x_df['p-p'],
                z=x_df['x-n'],
                mode="markers",
                text=x_df.index,
                hovertemplate='Piemērots: %{x:.2f}<br>Viegls: %{y:.2f}<br>Nepiemērots: %{z:.2f}<extra>%{text}</extra>',
                marker=dict(size=8, symbol="circle", color=krasa)  # color=student_df, colorscale='balance'
            ),
        ])

        fig.update_layout(
            #             template='seaborn',
            scene_camera=camera,
            scene=dict(
                xaxis_title="Piemērots",
                yaxis_title="Viegls",
                zaxis_title="Nepiemērots",
                xaxis=dict(
                    nticks=6, range=[0, 1],
                    backgroundcolor="rgb(200, 200, 230)",
                    gridcolor="white",
                    showbackground=True,
                    zerolinecolor="white",
                    showspikes=False),
                yaxis=dict(
                    nticks=6, range=[0, 1],
                    backgroundcolor="rgb(230, 200,230)",
                    gridcolor="white",
                    showbackground=True,
                    zerolinecolor="white",
                    showspikes=False),
                zaxis=dict(
                    nticks=6, range=[0, 1],
                    backgroundcolor="rgb(230, 230,200)",
                    gridcolor="white",
                    showbackground=True,
                    zerolinecolor="white",
                    showspikes=False),
            ),
            height=700,
            margin=dict(
                r=0, l=0,
                b=0, t=0),
        )
        return fig

    fig1 = final_aggregation('section', df, ab)
    fig2 = final_aggregation('lessonid', df, ab)
    fig3 = final_aggregation('user_id', df, ab)

    return fig1, fig2, fig3, temas, number_of_students, pari, summa, value


# -------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run_server(debug=True)
