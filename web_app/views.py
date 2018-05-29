from django.shortcuts import render
import json

file = open("/home/aptitudeweb/aptitudeweb/web_app/static/data/MainJson.txt", "r")
string = file.read()
LIST_ITEMS = json.loads(string)


def dictionary(nbr):
    dict1 = {
        1: 'first',
        2: 'second',
        3: 'third',
        4: 'forth',
        5: 'fifth'
    }
    return dict1[nbr]


def topic_list(request,alias="" ):
    list_items, a = get_topic_data(alias, 0)
    return render(request, 'home/topic_list.html', {'list': list_items})


def topic_menu(request, alias="", topic_id=0):
    list_items = None
    topic_data = {}
    list_items, topic_data = get_topic_data(alias, topic_id)
    if topic_data:
        return render(request, 'home/topic_menu.html', {'data': topic_data, 'topic_id': topic_id})
    else:
        return render(request, 'home/topic_list.html', {'list': list_items})


def paper_list(request, alias="", topic_id=0):
    list_items = None
    topic_data = {}
    list_items, topic_data = get_topic_data(alias, topic_id)
    if topic_data:
        return render(request, 'home/paper_list.html', {'data': topic_data, 'topic_id': topic_id,  'alias':alias})
    else:
        return render(request, 'home/topic_list.html', {'list': list_items})


def paper(request, paper_nbr=1, alias="",topic_id=0, q_nbr=1):
    curr = int(q_nbr)
    q_nbr = int(q_nbr)
    list_items = None
    topic_data = {}
    if int('1')<=q_nbr<=int('20'):
        paper_nbr=1
        if curr == 1:
            prev = 1
        else:
            curr = curr
            prev = curr - 1
        next = curr + 1
        count = get_questions_per_page(alias, topic_id, paper_nbr)
        last = count
    else:
        if q_nbr%20==0:
            paper_nbr = q_nbr/20
        else:
            paper_nbr = int(1) + int((q_nbr / 20))
        curr = 20 * (int(paper_nbr) - int(1)) + 1
        if curr == q_nbr:
            curr = q_nbr
            next = curr + 1
            prev = curr
        else:
            curr = q_nbr
            next = curr + 1
            prev = curr - 1
        count = get_questions_per_page(alias, topic_id, paper_nbr)
        last = 20 * (int(paper_nbr) - int(1)) + count

    list_items, topic_data = get_topic_data(alias, topic_id)
    url = '/home/aptitudeweb/aptitudeweb/web_app/templates/' + topic_data['baseQuestionsUrl'] + str(curr) + '.html'
    file = open(url, "r")
    string = file.read()
    import re
    string = re.sub("<h2>.*Question.*<\/h\d>",'',string)
    if topic_data:
        return render(request, 'home/question.html',
                      {'data': topic_data, 'curr': curr, 'prev': prev, 'next': next, 'string': string.replace("<div>",'<div class="div2">'), 'count': count,
                       'paper_nbr': paper_nbr, 'last': last, 'url':url})
    else:
        return render(request, 'home/topic_list.html', {'list': list_items})


def get_topic_data(alias='', topic_id=0):
    list_items = LIST_ITEMS
    topic_data1 = {}
    if alias:
        for each in list_items:
            if str(each['alias']) == alias:
                alias = alias
                topic_data1 = each
                break
    elif topic_id:
        for each in list_items:
            if str(each['topicId']) == topic_id:
                topic_id = topic_id
                topic_data1 = each
                break
    return list_items, topic_data1


def tutorial(request, alias="", topic_id=0):
    list_items, topic_data = get_topic_data(alias,topic_id)
    return render(request, topic_data['tutorialUrl'])


def formula(request, alias="", topic_id=0):
    list_items, topic_data = get_topic_data(alias, topic_id)
    return render(request, topic_data['formulaeUrl'])


def get_questions_per_page(alias,topic_id, paper_nbr):
    list_items, topic_data = get_topic_data(alias,topic_id)
    last = topic_data[dictionary(paper_nbr) + "QuestionPaperCount"]
    return last


def tutorial1(request, alias="",topic_id=0):
    list_items, topic_data = get_topic_data(alias,topic_id)
    url = '/home/aptitudeweb/aptitudeweb/web_app/templates/' + topic_data['tutorialUrl']
    file = open(url, "r")
    string = file.read()
    return render(request, 'home/tutorial.html', {'string':string, 'data':topic_data})


def formula1(request, alias="",topic_id=0):
    list_items, topic_data = get_topic_data(alias,topic_id)
    url = '/home/aptitudeweb/aptitudeweb/web_app/templates/' + topic_data['formulaeUrl']
    file = open(url, "r")
    string = file.read()
    return render(request, 'home/formula.html', {'string':string, 'data':topic_data})
