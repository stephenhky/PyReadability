import argparse
import metrics.flesch as f

def get_argparser():
    parser = argparse.ArgumentParser(description='Calculate the readability indices of the given text documents.')
    parser.add_argument('filepaths', nargs='+', help='paths of the text files.')
    return parser

if __name__ == '__main__':
    parser = get_argparser()
    args = parser.parse_args()

    for filepath in args.filepaths:
        text = open(filepath, 'rb').read()
        print 'Filepath: ', filepath
        word_count, sent_count, syllable_count = f.text_statistics(text)
        print 'Word count = ', word_count
        print 'Sentence count = ', sent_count
        print 'Syllable count = ', syllable_count
        print 'Flesch readability ease = ', f.flesch_formula(word_count, sent_count, syllable_count)
        print 'Flesch-Kincaid grade level = ', f.fk_formula(word_count, sent_count, syllable_count)