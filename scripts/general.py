def is_annotation_line(line):
    """Returns True if this line corresponds to a annotation line in the
    Webanno TSV file, False otherwise"""
    if line.strip().startswith('#') or line.strip() == '':
        return False
    return True


def get_labels_list(annots_file):
    """Get list of labels from Webanno TSV annotation file. All labels are
    normalized to 'RADLEX'."""

    with open(annots_file) as f:
        annots = f.readlines()

    annots = filter(lambda line: is_annotation_line(line), annots)
    annots = map(lambda line: line.strip().split('\t'), annots)

    labels = map(lambda line: line[-1], annots)

    for i, label in enumerate(labels):
        if label != 'O' and label != '_':
            labels[i] = 'RADLEX'

    return labels
