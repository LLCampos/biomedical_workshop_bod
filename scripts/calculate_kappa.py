import sklearn.metrics
import itertools
import os
import sys
from prettytable import PrettyTable

from general import get_labels_list

"""
Creates a table of Cohen's kappa agreement scores between all the users given
in the arguments.


Usage

python calculate_kappa.py [path_to_annotations] [list_of_usernames]

Example:

python calculate_kappa.py ../annotations/crowd_annotations/ user1 user2 user3

"""


def calculate_kappa(user1, user2, project_path):
    """Calculates kappa between two users. Aggregates annotations from all files
    annotated and then annotates usual kappa. It ignores files that were not
    annotated by both users."""

    files_annotated = os.listdir(project_path)

    total_labels1 = []
    total_labels2 = []

    for file_annotated in files_annotated:

        error_message = 'User {} didn\'t annotate file {}.'

        file_annotated_by_both = True

        try:
            labels1 = get_labels_list('{}/{}/{}.tsv'.format(
                project_path,
                file_annotated, user1)
            )
        except IOError:
            print error_message.format(user1, file_annotated)
            file_annotated_by_both = False

        try:
            labels2 = get_labels_list('{}/{}/{}.tsv'.format(
                project_path,
                file_annotated, user2)
            )
        except IOError:
            print error_message.format(user2, file_annotated)
            file_annotated_by_both = False

        if file_annotated_by_both:
            total_labels1 += labels1
            total_labels2 += labels2

    assert len(total_labels1) == len(total_labels2)
    return sklearn.metrics.cohen_kappa_score(total_labels1, total_labels2)


def get_all_kappas(usernames_list, project_path):
    """Returns a dictionary with values of Cohen's kappa between all pairs of
    users"""

    all_kappas = {}

    all_pairs = list(itertools.combinations(usernames_list, 2))
    for pair in all_pairs:
        all_kappas[pair] = round(calculate_kappa(pair[0], pair[1], project_path), 2)

    return all_kappas


def create_agreement_table(project_path, usernames_list):
    """project_path is the path to the project folder exported from the Webanno app."""

    all_kappas = get_all_kappas(usernames_list, project_path)

    table = PrettyTable()
    table.field_names = ['Users'] + usernames_list

    for i, user1 in enumerate(usernames_list):
        row = [user1]

        for j, user2 in enumerate(usernames_list):
            if i == j:
                row.append('-')
            elif i < j:
                row.append(all_kappas[(user1, user2)])
            else:
                row.append('-')

        assert len(row) == len(usernames_list) + 1

        table.add_row(row)

    table.format = True
    html_table = table.get_html_string()
    with open('agreement_scores.html', 'w') as f:
        f.write(html_table)

    print table


if __name__ == '__main__':
    project_path = sys.argv[1]
    usernames_list = sys.argv[2:]

    create_agreement_table(project_path, usernames_list)
