import requests
from bs4 import BeautifulSoup
import pprint
import sys


# variables
baseURL = 'https://news.ycombinator.com/news'
main_res = requests.get(baseURL)
main_soup = BeautifulSoup(main_res.text, 'html.parser')

links = main_soup.select('.storylink')     #dot stands for a class
subtext = main_soup.select('.subtext')
main_page = 1
full_list_of_stories = []


# how many pages of stories do you want to check
try:
    how_many_pages = sys.argv[1]
except IndexError:
    how_many_pages = 3


# sort stories by popularity
def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k: k['votes'], reverse=True)


# fcn which creates customized list of stories
def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace('points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


# go to the next page of the website
def next_page_fcn(pageNum):
    res = requests.get(f'{baseURL}?p={pageNum}')
    soup = BeautifulSoup(res.text, 'html.parser')
    return main(soup, how_many_pages)



def main(soup, stop):
    next_page = soup.select('.morelink')

    for i, j in enumerate(next_page):
        hrefNP = next_page[i].get('href', None)

    next_p_num = int(hrefNP.replace('news?p=', '')) #current_page number = next_p_num - 1


    if next_p_num <= stop:
        list_of_stories = create_custom_hn(links, subtext)
        # pprint.pprint(list_of_stories)
        for item in list_of_stories:
            full_list_of_stories.append(item)
        return next_page_fcn(next_p_num)
    else:
        pprint.pprint(sort_stories_by_votes(full_list_of_stories))
        return 0


main(main_soup, how_many_pages)


