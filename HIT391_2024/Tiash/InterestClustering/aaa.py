

def kmeans_clustering(X, n_clusters):
    """
    Applies K-means clustering.

    Parameters:
    X (pd.DataFrame): Feature matrix.
    n_clusters (int): Number of clusters.

    Returns:
    labels (np.ndarray): Cluster labels.
    """
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    labels = kmeans.fit_predict(X)
    return labels


def hierarchical_clustering(X, n_clusters):
    """
    Applies Hierarchical clustering.

    Parameters:
    X (pd.DataFrame): Feature matrix.
    n_clusters (int): Number of clusters.

    Returns:
    labels (np.ndarray): Cluster labels.
    """
    hierarchical = AgglomerativeClustering(n_clusters=n_clusters)
    labels = hierarchical.fit_predict(X)
    return labels


def evaluate_clustering(X, labels):
    """
    Evaluates the clustering results using silhouette score.

    Parameters:
    X (pd.DataFrame): Feature matrix.
    labels (np.ndarray): Cluster labels.

    Returns:
    silhouette (float): Silhouette score.
    """
    silhouette = silhouette_score(X, labels)
    return silhouette

# Main workflow


def main(filepath):
    # Step 1: Data Preprocessing
    X, y = load_and_preprocess_data(filepath)

    # Determine the number of clusters (e.g., based on 'Group' column)
    n_clusters = len(np.unique(y))

    # Step 2: K-means Clustering
    kmeans_labels = kmeans_clustering(X, n_clusters)
    kmeans_silhouette = evaluate_clustering(X, kmeans_labels)
    print(f"K-means Silhouette Score: {kmeans_silhouette}")

    # Step 3: Hierarchical Clustering
    hierarchical_labels = hierarchical_clustering(X, n_clusters)
    hierarchical_silhouette = evaluate_clustering(X, hierarchical_labels)
    print(
        f"Hierarchical Clustering Silhouette Score: {hierarchical_silhouette}")


# Example usage
# Replace 'path/to/your/dataset.csv' with the actual path to your dataset
main('path/to/your/dataset.csv')
