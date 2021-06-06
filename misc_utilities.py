import itertools

import matplotlib.pyplot as plt
import seaborn as sns
from dtreeviz.trees import dtreeviz
from sklearn.metrics import (accuracy_score, precision_score, recall_score, f1_score, confusion_matrix,
                             ConfusionMatrixDisplay, roc_curve, auc, mean_squared_error, r2_score, mean_absolute_error)


def plot_hist_all_columns(df):
    """
    Plots a series of histograms per column
    :param df: dataframe to plot with
    """
    columns = df.columns[:len(df.columns)]
    plt.subplots(figsize=(18, 24))
    length = len(columns)
    for i, j in itertools.zip_longest(columns, range(length)):
        plt.subplot(int(length / 2), 3, j + 1)
        plt.subplots_adjust(wspace=0.2, hspace=0.5)
        df[i].hist(bins=20, edgecolor='black')
        plt.title(i)
    plt.show()


def classification_metrics(true_labels, predicted_labels, labels=None, f1_weighting='binary', multiclass=True):
    """
    Returns a dictionary of common classification metrics. Implemented as sklearn's classification report doesn't offer
     enough control over parameters.
    :param true_labels: true values of target vector
    :param predicted_labels: predicted values of target vector
    :param labels: full set of labels from target vector
    :param f1_weighting: how the F1 score is weighted. Choice = 'micro', 'macro', 'samples','weighted', 'binary' or None
    :param multiclass: Whether you have binary or multiple classes
    :return: dictionary of metric results
    """
    pr_weighting = 'weighted' if multiclass else 'binary'
    return {'accuracy': accuracy_score(true_labels, predicted_labels),
            'precision': precision_score(true_labels, predicted_labels, labels=labels, average=pr_weighting),
            'recall': recall_score(true_labels, predicted_labels, labels=labels, average=pr_weighting),
            'F1': f1_score(true_labels, predicted_labels, labels=labels, average=f1_weighting)}


def regression_metrics(true_labels, predicted_labels):
    """
    Returns a dictionary of common regression metrics.
    :param true_labels: true values of target vector
    :param predicted_labels: predicted values of target vector
    :return: dictionary of metric results
    """
    return {'MSE': mean_squared_error(true_labels, predicted_labels, squared=True),
            'RMSE': mean_squared_error(true_labels, predicted_labels, squared=False),
            'MAE': mean_absolute_error(true_labels, predicted_labels),
            'R2': r2_score(true_labels, predicted_labels)}


def plot_conf_matrix(true_labels, predicted_labels):
    """
    Plots a confusion matrix
    :param true_labels: true values of target vector
    :param predicted_labels: predicted values of target vector
    """
    conf = confusion_matrix(true_labels, predicted_labels)
    ConfusionMatrixDisplay(conf).plot()


def plot_correlation_matrix(df):
    """
    Plots a correlation matrix
    :param df: Dataframe to use
    """
    plt.figure(figsize=(25, 25))
    sns.heatmap(df.corr(), annot=True, square=True, linewidths=2)


def plot_decision_tree(tree_model, X, y, feature_names, class_names=None):
    """
    Plots a decision tree, and saves it as a SVG file.
    :param tree_model: Decision tree (Random Forest works too, just be sure to only select 1 estimator)
    :param X: Features
    :param y: Labels
    :param feature_names: Column names
    :param class_names: Label names
    :return: graph
    """
    if class_names is None:
        class_names = []
    viz = dtreeviz(tree_model, X, y,
                   target_name="target",
                   feature_names=feature_names,
                   class_names=class_names)
    viz.save("decision_tree.svg")
    return viz


def plot_roc_curve(true_labels, predicted_labels):
    """
    Plots a ROC curve with its AUC
    :param true_labels: true values of target vector
    :param predicted_labels: predicted values of target vector
    """
    fpr, tpr, threshold = roc_curve(true_labels, predicted_labels)
    roc_auc = auc(fpr, tpr)

    plt.title('ROC')
    plt.plot(fpr, tpr, 'b', label='AUC = %0.2f' % roc_auc)
    plt.legend(loc='lower right')
    plt.plot([0, 1], [0, 1], 'r--')
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.ylabel('True Positive Rate')
    plt.xlabel('False Positive Rate')
    plt.show()


def plot_fit_curves(fit_history, train_metric='loss', val_metric='val_loss', remove_first=True):
    """
    Plots the history of training a model into a line graph
    :param fit_history: history object from model.fit()
    :param train_metric: what to use for the training metrics (only use if you have custom metrics)
    :param val_metric: what to use for the validation metrics (only use if you have custom metrics)
    :param remove_first: whether to remove the first epoch from the history. This can be useful if your first epoch
    has a extremely high score, which messes with the visuals of the plot
    """
    if remove_first:
        train_hist = fit_history.history[train_metric][1:]
        val_hist = fit_history.history[val_metric][1:]
    else:
        train_hist = fit_history.history[train_metric]
        val_hist = fit_history.history[val_metric]
    plt.plot(train_hist)
    plt.plot(val_hist)
    plt.title('Training curve')
    plt.ylabel(train_metric)
    plt.xlabel(val_metric)
    plt.legend(['train', 'val'], loc='upper left')
    plt.show()
