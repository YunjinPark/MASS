import unicodedata

TOKEN_TYPE_HANGUL = 'h'
TOKEN_TYPE_ALPHA = 'a'
TOKEN_TYPE_NUMBER = 'n'
TOKEN_TYPE_ETC = 'e'
TOKEN_TYPE_SPACE = 'e'
TOKEN_TYPE_FOREIGN = 'f'

# charactor code
CHARACTERSET_DICT = {"UNKNOWN":TOKEN_TYPE_ETC,
                     "SPACE":TOKEN_TYPE_SPACE,
                     "DIGIT":TOKEN_TYPE_NUMBER,
                     "HANGUL":TOKEN_TYPE_HANGUL,
                     "LATIN":TOKEN_TYPE_ALPHA,
                     "GREEK":TOKEN_TYPE_FOREIGN,
                     "ARABIC":TOKEN_TYPE_FOREIGN,
                     "HEBREW":TOKEN_TYPE_FOREIGN,
                     "CYRILLIC":TOKEN_TYPE_FOREIGN,
                     "HIRAGANA":TOKEN_TYPE_FOREIGN,
                     "KATAKANA":TOKEN_TYPE_FOREIGN,
                     "CJK":TOKEN_TYPE_ETC }

KOREAN_CORPUS_EXCLUDE_CHARACTERSET_DICT = {"UNKNOWN":TOKEN_TYPE_ETC,
                     "GREEK":TOKEN_TYPE_FOREIGN,
                     "ARABIC":TOKEN_TYPE_FOREIGN,
                     "HEBREW":TOKEN_TYPE_FOREIGN,
                     "CYRILLIC":TOKEN_TYPE_FOREIGN,
                     "HIRAGANA":TOKEN_TYPE_FOREIGN,
                     "KATAKANA":TOKEN_TYPE_FOREIGN,
                     "CJK":TOKEN_TYPE_ETC }

def token_split_by_char_type(input_token):
  cur_token_type = None
  last_token_type = None
  cur_token = ''
  token_list = []

  for i, c in enumerate(list(input_token)):
    try:
      print('>', c, ' ', unicodedata.name(c))
      name = unicodedata.name(c)
      charType = name.split(' ')[0]
      if not charType in CHARACTERSET_DICT:
        charType = "UNKNOWN"
      cur_token_type = CHARACTERSET_DICT[charType]
      if cur_token_type == TOKEN_TYPE_ALPHA:
        c = c.lower()
    except TypeError:
      print('TypeError: ', c)
      continue

    if last_token_type:
      if cur_token_type == last_token_type:
        cur_token = cur_token + c
      else:
        token_list.append((cur_token, last_token_type))
        last_token_type = cur_token_type
        cur_token = c
    else:
      last_token_type = cur_token_type
      cur_token = c

  token_list.append((cur_token, cur_token_type))

  return token_list


def filter_str_by_chartype(input_sentence, filter_type_dict=KOREAN_CORPUS_EXCLUDE_CHARACTERSET_DICT):
    output_list = []
    for c in list(input_sentence):
        try:
            name = unicodedata.name(c)
            charType = name.split(' ')[0]
            if charType not in filter_type_dict:
                output_list.append(c)
        except ValueError:  # 간혹 unicodedata.name에 에러 발생시키는 특수문자도 출현한다..
            continue

    return ''.join(output_list)


# print('굿𠀋1996 !!\n')
# print(filter_str_by_chartype('굿𠀋1996 !!\n'))
# print(filter_str_by_chartype('11🍡      -31818\n'))