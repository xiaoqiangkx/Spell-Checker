#coding=utf-8

import re


def text_cleaner(text, uncase=False):
    if uncase:
        text = text.lower()
    # Clean the text

    # irregular single quotes
    text = re.sub(r"[’‘]", "'", text)
    # usual abbr
    text = text.replace("it's", "it is")
    text = text.replace("that's", "that is")
    text = text.replace("there's", "there is")
    text = text.replace("here's", "here is")
    text = text.replace("he's", "he is")
    text = text.replace("she's", "she is")
    text = text.replace("what's", "what is")
    text = text.replace("who's", "who is")
    text = text.replace("how's", "how is")
    text = text.replace("where's", "where is")
    text = text.replace("let's", "let us")
    text = text.replace("i'm", "i am")
    text = text.replace("won't", "will not")
    text = text.replace("ain't", "am not")
    text = text.replace("'d", " would")
    text = text.replace("'ve", " have")
    text = text.replace("'ll", " will")
    text = text.replace("n't", " not")
    text = text.replace("'re", " are")
    # new line mark in questions
    text = text.replace('<br>', ' ')
    # other punctuations
    text = re.sub(r"[,^!:;+=\.\/\(\)\"\'\-\?\\？\n\r]", " ", text)
    # blanks
    text = re.sub('\s+', ' ', text).strip()

    return text


def asr_cleaner(text, caseonly=False):
    text = ' ' + text + ' '
    text = text.replace(" i'm ", " I'm ")
    text = text.replace(" i've ", " I've ")
    text = text.replace(" i'll ", " I'll ")
    text = text.replace(" i'd ", " I'd ")
    text = text.replace(" i ", " I ")

    if not caseonly:
        # # usual abbr
        text = text.replace(" it's ", " it is ")
        text = text.replace(" that's ", " that is ")
        text = text.replace(" this's ", " this is ")
        text = text.replace(" there's ", " there is ")
        text = text.replace(" here's ", " here is ")
        text = text.replace(" he's ", " he is ")
        text = text.replace(" she's ", " she is ")
        text = text.replace(" what's ", " what is ")
        text = text.replace(" who's ", " who is ")
        text = text.replace(" how's ", " how is ")
        text = text.replace(" where's ", " where is ")
        text = text.replace(" let's ", " let us ")
        text = text.replace(" won't ", " will not ")
        text = text.replace(" ain't ", " am not ")
        text = text.replace(" can't ", " can not ")
        text = text.replace(" gonna ", " going to ")
        text = text.replace(" wanna ", " want to ")
        # text = text.replace("'d", " would")
        # text = text.replace("'ve", " have")
        # text = text.replace("'ll", " will")
        # text = text.replace("n't", " not")
        # text = text.replace("'re", " are")

    # # blanks
    # text = re.sub('\s+', ' ', text).strip()

    return text.strip()


class BColors(object):
    HEADER = u'\033[95m'
    OKBLUE = u'\033[94m'
    OKGREEN = u'\033[92m'
    WARNING = u'\033[93m'
    FAIL = u'\033[91m'
    ENDC = u'\033[0m'
    BOLD = u'\033[1m'
    UNDERLINE = u'\033[4m'
    WHITE = u'\033[37m'
    YELLOW = u'\033[33m'
    GREEN = u'\033[32m'
    BLUE = u'\033[34m'
    CYAN = u'\033[36m'
    RED = u'\033[31m'
    MAGENTA = u'\033[35m'
    BLACK = u'\033[30m'
    BHEADER = BOLD + u'\033[95m'
    BOKBLUE = BOLD + u'\033[94m'
    BOKGREEN = BOLD + u'\033[92m'
    BWARNING = BOLD + u'\033[93m'
    BFAIL = BOLD + u'\033[91m'
    BUNDERLINE = BOLD + u'\033[4m'
    BWHITE = BOLD + u'\033[37m'
    BYELLOW = BOLD + u'\033[33m'
    BGREEN = BOLD + u'\033[32m'
    BBLUE = BOLD + u'\033[34m'
    BCYAN = BOLD + u'\033[36m'
    BRED = BOLD + u'\033[31m'
    BMAGENTA = BOLD + u'\033[35m'
    BBLACK = BOLD + u'\033[30m'

    @staticmethod
    def cleared(s):
        return re.sub(u"\033\[[0-9][0-9]?m", u"", s)


def red(message):
    return BColors.RED + unicode(message) + BColors.ENDC


def b_red(message):
    return BColors.BRED + unicode(message) + BColors.ENDC


def blue(message):
    return BColors.BLUE + unicode(message) + BColors.ENDC


def b_yellow(message):
    return BColors.BYELLOW + unicode(message) + BColors.ENDC


def green(message):
    return BColors.GREEN + unicode(message) + BColors.ENDC


def b_green(message):
    return BColors.BGREEN + unicode(message) + BColors.ENDC
