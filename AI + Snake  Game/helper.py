import matplotlib.pyplot as plt

plt.ion()

def plot(scores, mean_scores):
    plt.clf()

    # Create the plot
    plt.title('Training...')
    plt.xlabel('Number of Games')
    plt.ylabel('Score')
    plt.plot(scores, label='Scores')
    plt.plot(mean_scores, label='Mean Scores')
    plt.ylim(ymin=0)
    plt.legend()

    latest_score = scores[-1]
    latest_mean_score = mean_scores[-1]
    plt.annotate(f'{latest_score:.2f}', (len(scores) - 1, latest_score), textcoords="offset points", xytext=(0,10), ha='center')
    plt.annotate(f'{latest_mean_score:.2f}', (len(mean_scores) - 1, latest_mean_score), textcoords="offset points", xytext=(0,10), ha='center')

    # Display the plot
    plt.pause(0.1) # Add a short pause to allow the plot to update 