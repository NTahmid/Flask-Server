from flask import Flask,render_template, request, jsonify, redirect
from utils import get_vizualization_dictionary,get_visualization_folderpath,get_chart_filepath
import json
import copy
import time


# EB looks for an 'application' callable by default.
application = Flask(__name__)
application.config['SECRET_KEY'] = 'some_random_secret'  # Required for session to work

d3_code = ""
data_text= ""
topics= ""
expert_process = ""
education_level = ""
visualization_level = ""
topics_to_be_annotated = ""

survey1_answers = {}
survey2_answers = {}

new_topic_explanation = ""
new_annotated_code = ""
saved_survey_answers = {}

saved_topic_explanations= {}
saved_topic_charts= {}

demographics = {}
participant_info = {}
entry_username = ""

selected_llm_curriculum = {}
selected_human_curriculum = {}


@application.route('/')
def index():
    #session['topic_no'] = 1  # Initialize topic_no in the session
    return render_template('home2.html');


@application.route('/demographics')
def demographics():
    return render_template('demographics.html');

@application.route('/info', methods=['POST'])
def info():
    global demographics
    
    education_level = request.form.get('edRadioOptions')
    viz_level = request.form.get('vizRadioOptions')
    work_level = request.form.get('workRadioOptions')

    demographics_info = {
        'education_level': education_level,
        'viz_level':viz_level,
        'work_level':work_level
    }

    demographics = demographics_info
    
    return render_template('info.html');

@application.route('/curriculum/1')
def chart():
    
    global d3_code,selected_llm_curriculum,selected_human_curriculum


    curriculum_filename = 'curriculum2.txt'
    human_curriculum_filename = 'curriculum1.txt'

    folderpath = get_visualization_folderpath(1)
    chart_filepath = get_chart_filepath(1)

    # folderpath = get_visualization_folderpath(2)
    # chart_filepath = get_chart_filepath(2)

    # folderpath = get_visualization_folderpath(4)
    # chart_filepath = get_chart_filepath(4)
    
    curriculum_filepath = folderpath+'/'+curriculum_filename
    curriculum_data = ''
    chart_code = ''

    human_curriculum_filepath = folderpath+'/'+human_curriculum_filename
    human_curriculum_data = ''

    with open(curriculum_filepath) as f:
        curriculum_data = f.read()
    with open(human_curriculum_filepath) as f:
        human_curriculum_data = f.read()
    with open(chart_filepath) as f:
        chart_code = f.read()
    
    curriculum = json.loads(curriculum_data)
    human_curriculum = json.loads(human_curriculum_data)


    d3_code = chart_code
    selected_llm_curriculum = curriculum
    selected_human_curriculum = human_curriculum


    return render_template('chart.html',chart = chart_code, llm_topics = curriculum, curriculum="first")


    # # curriculum_keys = list(curriculum.keys())
    
    # global d3_code,data_text,topics,topics_to_be_annotated,saved_topic_explanations,saved_topic_charts,participant_info,entry_username

    # # participant_name = request.form.get('nameTextBox');
    # # participant_id = request.form.get('idTextBox');
    # # selected_chart = request.form.get('vizSelectDropdown');

    # # username = participant_id + participant_name
    # # info = {
    # #     'name':participant_name,
    # #     'id':participant_id,
    # #     'selected_chart':selected_chart
    # # }

    # # participant_info = info
    # # entry_username = username

    
    # #selected_chart = "Viz 2"
    # selected_chart_file = None
    # selected_chart_data = None
    # chart_code = None
    # chart_data = None
    # vizualization_dict = get_vizualization_dictionary();
    # selected_value = None
    # llm_topics = None
    # human_topics = None

    # for item in vizualization_dict:
    #     if selected_chart in item:
    #         selected_value = item[selected_chart]
    #         break

    # selected_chart_file = selected_value["filename"];
    # chart_filepath = os.path.join("chart-data", selected_chart_file);

    # with open(chart_filepath, 'r') as file:
    #     chart_code = file.read()

    # d3_code = chart_code


    # if selected_value["separate_data"] == True:
    #     selected_chart_data = selected_value["datafile"];
    #     data_filepath = os.path.join('chart-data',selected_chart_data);

    #     with open(data_filepath,'r') as file:
    #         chart_data = file.read()
    #     data_text = chart_data

    # llm_topics = {}

    # if selected_value["separate_data"] == True:
    #     llm_topics = curriculum_chart_with_seperate_data(chart_code,chart_data)
    # else:
    #     llm_topics = curriculum_chart_without_seperate_data(chart_code)

    # topics = llm_topics

    # topic_keys = list(topics.keys())
    # temp_topic_explanation = {}
    # temp_topic_charts = {}

    # for i in range(0,len(topic_keys)):
    #     temp_topic_explanation[topic_keys[i]] = ""
    #     temp_topic_charts[topic_keys[i]] = ""
    # # for i in range(0,len(topic_keys)):
    # #     temp_topic_explanation[topic_keys[i]] = ""
    # #     temp_topic_charts[topic_keys[i]] = ""

    # saved_topic_charts = temp_topic_charts
    # saved_topic_explanations = temp_topic_explanation

    # topics_to_be_annotated = is_annotation_needed(llm_topics,chart_code,data_text)

    # # print(topics)

    # # print(topics_to_be_annotated)

    # # llm_topics = {'1': 'Understanding the Basics of Charts',
    # #                       '2': 'Identifying Different Types of Charts',
    # #                       '3': 'Reading the Chart Title and Subtitle',
    # #                       '4': 'Interpreting the X and Y Axis',
    # #                       '5': 'Understanding the Data Points and Bars',
    # #                       '6': 'Reading the Legend',
    # #                       '7': 'Analyzing the Data Trends',
    # #                       '8': 'Drawing Conclusions from the Chart',
    # #                       '9': 'Understanding the Color Coding in Charts',
    # #                       '10': 'Learning about Data Sorting',
    # #                       '11': 'Understanding the Scale and Range of Charts',
    # #                       '12': 'Interpreting the Data Values',
    # #                       '13': 'Understanding the Padding in Charts',
    # #                       '14': 'Learning about Data Transformation',
    # #                       '15': 'Understanding the Use of Scripts in Charts'
    # #                       }


    # return render_template('chart.html',chart = chart_code, llm_topics = llm_topics)


# @app.route('/get-topic-explanation',methods=['POST'])
# def get_topic_explanation():
#     content = request.get_json()
#     topic_name = content['topic']
#     response = contextual_explanation(topic_name,d3_code,data_text);
#     return jsonify(response)


# @app.route('/get-modified-chart',methods=['POST'])
# def get_modified_chart():
#     global topics_to_be_annotated, d3_code, data_text
#     content = request.get_json()
#
#     print(content)
#
#     topic_name = content['topic']
#     topic_explanation = content['explanation']
#     index = content['index']
#
#     response = ""
#     if topics_to_be_annotated[str(index)] == "No":
#         response = "No"
#     else:
#         response = annotate_code(topic_name,topic_explanation,d3_code,data_text)
#     return jsonify(response)



@application.route('/curriculum/2')
def chart2():
    
    global d3_code,selected_human_curriculum

    return render_template('chart.html',chart = d3_code, llm_topics = selected_human_curriculum, curriculum="second")


@application.route('/send-survey1-curriculum1-answer',methods=['POST'])
def process_survey1_answers1():
    
    # global survey1_answers
    # content = request.get_json()
    # print(content)
    # answers = content["answers"]
    # survey1_answers = answers
    # print(answers)
    
    return redirect("/curriculum/2")


@application.route('/send-survey1-curriculum2-answer', methods=['POST'])
def process_survey1_answers():
    # global survey1_answers
    # content = request.get_json()
    # print(content)
    # answers = content["answers"]
    # survey1_answers = answers
    # print(answers)

    return redirect("/description")



@application.route('/description')
def description():

    #global topics,d3_code,data_text,topics_to_be_annotated,saved_topic_explanations,saved_topic_charts

    curriculum_filename = 'curriculum2.txt'
    folderpath = get_visualization_folderpath(1)
    annotated_chart_filepath = folderpath+'/'+'annotated_chart1.html'

    curriculum_filepath = folderpath + '/' + curriculum_filename
    explanation_filepath = folderpath + '/' + 'curriculum2_explanation.txt'
    curriculum_data = ''
    chart_code = ''
    explanation_data = ''

    with open(curriculum_filepath) as f:
        curriculum_data = f.read()
    with open(annotated_chart_filepath) as f:
        chart_code = f.read()
    with open(explanation_filepath) as f:
        explanation_data = f.read()

    curriculum = json.loads(curriculum_data)
    explanation = json.loads(explanation_data)

    init_topic_explanation = explanation['1'];

    return render_template('description.html', topics=curriculum, init_topic_explanation=init_topic_explanation, html_code=chart_code, topic_index=1, saved_answers={})


@application.route('/topic-change-click',methods=['POST'])
def topic_change_func():
    global topics, d3_code, data_text, topics_to_be_annotated, new_topic_explanation, new_annotated_code, saved_survey_answers, saved_topic_charts, saved_topic_explanations

    content = request.get_json()
    new_index = str(content['topic_index'])
    #survey_answers = content['answers']
    

    # html_code = d3_code

    # if topics_to_be_annotated[new_index] == 'Yes':
    #     annotated_code = annotate_code(topics[new_index],topic_explanation,d3_code,data_text)
    #     html_code = annotated_code


    #saved_survey_answers = survey_answers
    #print(saved_survey_answers)

    return jsonify(serverResponseString = new_index)


@application.route('/description/<int:topic_id>')
def description_two(topic_id):

    global topics,d3_code,data_text,topics_to_be_annotated,new_topic_explanation,new_annotated_code,saved_survey_answers

    curriculum_filename = 'curriculum2.txt'
    folderpath = get_visualization_folderpath(1)
    annotated_chart_filepath = folderpath + '/' + 'annotated_chart'+str(topic_id)+'.html'

    curriculum_filepath = folderpath + '/' + curriculum_filename
    explanation_filepath = folderpath + '/' + 'curriculum2_explanation.txt'
    curriculum_data = ''
    chart_code = ''
    explanation_data = ''

    with open(curriculum_filepath) as f:
        curriculum_data = f.read()
    with open(annotated_chart_filepath) as f:
        chart_code = f.read()
    with open(explanation_filepath) as f:
        explanation_data = f.read()

    curriculum = json.loads(curriculum_data)
    explanation = json.loads(explanation_data)

    new_topic_explanation = explanation[str(topic_id)];

    return render_template('description.html', topics=curriculum,init_topic_explanation = new_topic_explanation, html_code = chart_code, topic_index = topic_id, saved_answers = saved_survey_answers)


@application.route('/send-survey2-answer',methods=['POST'])
def process_survey2_answers():
    global survey2_answers
    content = request.get_json()
    print("jell")
    print(content)
    answers = content["answers"]
    survey2_answers = answers
    print(answers)
    
    # survey_answers_reference.set({
    #     "rere":{
    #         'demographic_info':demographics,
    #         'participant_info':participant_info,
    #         'survey1_answers':survey1_answers,
    #         'survey2_answers':survey2_answers
    #     }
    # })
    #print(demographics)
    return redirect("/final")


@application.route('/final')
def final_submit():
    #global demographics, participant_info, entry_username, survey_answers_reference, survey1_answers
    # survey_answers_reference.set({
    #     entry_username: {
    #         'demographic_info': demographics,
    #         'participant_info': participant_info,
    #         'survey1_answers': survey1_answers,
    #         'survey2_answers': survey2_answers
    #     }
    # })

    return render_template('final.html')
# # print a nice greeting.
# def say_hello(username = "World"):
#     return '<p>Hello %s!</p>\n' % username

# # some bits of text for the page.
# header_text = '''
#     <html>\n<head> <title>EB Flask Test</title> </head>\n<body>'''
# instructions = '''
#     <p><em>Hint</em>: This is a RESTful web service! Append a username
#     to the URL (for example: <code>/Thelonious</code>) to say hello to
#     someone specific.</p>\n'''
# home_link = '<p><a href="/">Back</a></p>\n'
# footer_text = '</body>\n</html>'



# # add a rule for the index page.
# application.add_url_rule('/', 'index', (lambda: header_text +
#     say_hello() + instructions + footer_text))

# # add a rule when the page is accessed with a name appended to the site
# # URL.
# application.add_url_rule('/<username>', 'hello', (lambda username:
#     header_text + say_hello(username) + home_link + footer_text))

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()