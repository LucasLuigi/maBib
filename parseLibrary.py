# -*-coding: utf-8 -*

import os
import wikipedia


class author:
    def __init__(self, name):
        self.name = name
        self.countries = {}
        self.countryCounter = 0


if __name__ == '__main__':
    print('- parseLibrary - \n')

    wikipedia.set_lang('fr')

    with open('list', 'r', encoding='utf-8') as listFile:
        listLines = listFile.readlines()

    results = []
    # workaround to replace the not in result condition
    uniqueAuthorList = []

    # Query
    print('# QUERY')
    for line in listLines:
        splittedLine = line.split(';', 1)
        authorFirstName = splittedLine[0].strip(' \n')
        authorSurName = splittedLine[1].strip(' \n')
        authorCompleteName = authorFirstName+' '+authorSurName

        authorPage = None
        categories = None

        print('> '+authorCompleteName)
        if authorCompleteName not in uniqueAuthorList:
            uniqueAuthorList.append(authorCompleteName)

            authorInst = author(authorCompleteName)
            try:
                authorPage = wikipedia.page(title=authorCompleteName)
            except Exception:
                print('ERROR: search #1')
                try:
                    # Relaunching name with the surname only
                    authorPage = wikipedia.page(
                        title=authorSurName, auto_suggest=False)
                except Exception:
                    print('ERROR: search #2')
                    authorPage = None

            if authorPage != None:
                print('DEBUG: Found page '+authorPage.title+': ')

                countryFound = (authorPage.summary.find(
                    'français') != -1 or authorPage.summary.find('Français') != -1)
                if countryFound:
                    authorInst.countryCounter += 1
                authorInst.countries['fr'] = countryFound

                countryFound = (authorPage.summary.find('anglais') != -1
                                or authorPage.summary.find('Anglais') != -1
                                or authorPage.summary.find('britannique') != -1
                                or authorPage.summary.find('Britannique') != -1)
                if countryFound:
                    authorInst.countryCounter += 1
                authorInst.countries['uk'] = countryFound

                countryFound = (authorPage.summary.find(
                    'israélien') != -1 or authorPage.summary.find('Israélien') != -1)
                if countryFound:
                    authorInst.countryCounter += 1
                authorInst.countries['is'] = countryFound

                countryFound = (authorPage.summary.find(
                    'espagnol') != -1 or authorPage.summary.find('Espagnol') != -1)
                if countryFound:
                    authorInst.countryCounter += 1
                authorInst.countries['es'] = countryFound

                countryFound = (authorPage.summary.find(
                    'chinois') != -1 or authorPage.summary.find('Chinois') != -1)
                if countryFound:
                    authorInst.countryCounter += 1
                authorInst.countries['cn'] = countryFound

                countryFound = (authorPage.summary.find('russe') != -1
                                or authorPage.summary.find('Russe') != -1
                                or authorPage.summary.find('soviétique') != -1
                                or authorPage.summary.find('Soviétique') != -1)
                if countryFound:
                    authorInst.countryCounter += 1
                authorInst.countries['ru'] = countryFound

                countryFound = (authorPage.summary.find(
                    'américain') != -1 or authorPage.summary.find('Américain') != -1)
                if countryFound:
                    authorInst.countryCounter += 1
                authorInst.countries['us'] = countryFound

            print('DEBUG: countries=', end='')
            print(authorInst.countries)

            results.append(authorInst)

        print('')

    # Analysis
    print('# ANALYSIS')
    if len(results) != len(uniqueAuthorList):
        print('ERROR: error during parsing! len(results) != len(uniqueAuthorList)')

    for result in results:
        if result.countryCounter == 0:
            print('WARNING: '+result.name+', no country found')
