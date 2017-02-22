import sys
import os
import sklearn.metrics

"""
Calculates Precision, Recall and F1-Score a group of o test annotations against
a group of gold annotations.

Usage

python compare_annotations.py [path to gold annotations folder] [path to test annotations folder]

Example:

python compare_annotations.py annotations/aggregated_annotations/ annotations/noble_coder_annotations/
"""


def is_annotation_line(line):
    """Returns True if this line corresponds to a annotation line in the Webanno TSV file, False otherwise"""
    if line.strip().startswith('#') or line.strip() == '':
        return False
    return True


def get_labels_list(annots_file):
    """Get list of labels from Webanno TSV annotation file. All labels are normalized to 'RADLEX'. """

    with open(annots_file) as f:
        annots = f.readlines()

    annots = filter(lambda line: is_annotation_line(line), annots)
    annots = map(lambda line: line.strip().split('\t'), annots)

    labels = map(lambda line: line[-1], annots)

    for i, label in enumerate(labels):
        if label != 'O' and label != '_':
            labels[i] = 'RADLEX'

    return labels


def compare_annotations(path_gold_annots_folder, path_test_annots_folder):
    """Arguments are paths to the folders containing the TSV annotations files.

    Assuming that folders have files with the same names."""

    files_gold_annots_names = os.listdir(path_gold_annots_folder)
    files_test_annots_names = os.listdir(path_test_annots_folder)

    if len(files_test_annots_names) < len(files_gold_annots_names):
        filenames = files_test_annots_names
    else:
        filenames = files_gold_annots_names

    true_labels = []
    pred_labels = []

    for filename in filenames:
        gold_file_path = path_gold_annots_folder + filename
        test_file_path = path_test_annots_folder + filename

        true_labels += get_labels_list(gold_file_path)
        pred_labels += get_labels_list(test_file_path)

    print "Precision: " + str(sklearn.metrics.precision_score(true_labels, pred_labels, pos_label='RADLEX'))
    print "Recall: " + str(sklearn.metrics.recall_score(true_labels, pred_labels, pos_label='RADLEX'))
    print "F1-Score: " + str(sklearn.metrics.f1_score(true_labels, pred_labels, pos_label='RADLEX'))


if __name__ == '__main__':
    gold_annotations_folder = sys.argv[1]
    test_annotations_folder = sys.argv[2]

    compare_annotations(gold_annotations_folder, test_annotations_folder)
