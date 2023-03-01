from hellonlp.ChineseWordSegmentation.utils import load_excel_only_first_sheet
f = 'data/data.xlsx'
contents = load_excel_only_first_sheet(f).fillna('')['content'].tolist()[:100]
print(len(contents))
#
#contents = ['23','dsad','dwq']
words = get_words(contents)
print(words[:100])
