def get_visualization_folderpath(viz_number):
    folderpath=''
    if viz_number == 1:
        folderpath = 'curriculum-data/viz1-bar'
    elif viz_number == 2:
        folderpath = 'curriculum-data/viz4-box'
    elif viz_number == 3:
        folderpath = 'curriculum-data/viz5-bubble'
    elif viz_number == 4:
        folderpath = 'curriculum-data/viz11-scatter-plot'

    return folderpath


def get_chart_filepath(viz_number):
    folderpath = ''
    if viz_number == 1:
        folderpath = 'curriculum-data/viz1-bar/bar-chart-grouped.html'
    elif viz_number == 2:
        folderpath = 'curriculum-data/viz4-box/box_plot_2.html'
    elif viz_number == 3:
        folderpath = 'curriculum-data/viz5-bubble/bubble-chart-1.html'
    elif viz_number == 4:
        folderpath = 'curriculum-data/viz11-scatter-plot/scatter-plot-2.html'

    return folderpath


def get_vizualization_dictionary():
    result = [
        {
            "Viz 1": {
                "filename": "bar-chart-grouped.html",
                "datafile": "",
                "separate_data": False
            }
        },
        {
            "Viz 2": {
                "filename": "bar-chart-horizontal.html",
                "datafile": "bar-chart-horizontal-data.txt",
                "separate_data":True
            }
        },
        {
            "Viz 3": {
                "filename": "bar-chart-standard.html",
                "datafile": "bar-chart-standard-data.txt",
                "separate_data":True
            }
        },
        {
            "Viz 4": {
                "filename": "box_plot_2.html",
                "datafile": "",
                "separate_data": False
            }
        },
        {
            "Viz 5": {
                "filename": "bubble-chart-1.html",
                "datafile": "",
                "separate_data": False
            }
        },
        {
            "Viz 6": {
                "filename": "bubble-chart-2.html",
                "datafile": "",
                "separate_data": False
            }
        },
        {
            "Viz 7": {
                "filename": "pi_plot_1.html",
                "datafile": "",
                "separate_data": False
            }
        },
        {
            "Viz 8": {
                "filename": "pi_plot_2.html",
                "datafile": "",
                "separate_data": False
            }
        },
        {
            "Viz 9": {
                "filename": "pi_plot_3.html",
                "datafile": "",
                "separate_data": False
            }
        },
        {
            "Viz 10": {
                "filename": "scatter-plot-1.html",
                "datafile": "scatter-plot-1-data.txt",
                "separate_data": True
            }
        },
        {
            "Viz 11": {
                "filename": "scatter-plot-2.html",
                "datafile": "scatter-plot-2-data.txt",
                "separate_data": True
            }
        }


    ]

    return result;