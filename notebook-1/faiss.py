import faiss
import numpy as np

dimension = 40    # dimensions of each vector
n = 20000    # number of vectors
np.random.seed(1)
db_vectors = np.random.random((n, dimension)).astype('float32')

nlist = 10  # number of clusters
quantiser = faiss.IndexFlatL2(dimension)
index = faiss.IndexIVFFlat(quantiser, dimension, nlist, faiss.METRIC_L2)

index.train(db_vectors)  # train on the database vectors
index.add(db_vectors)   # add the vectors and update the index
print(index.is_trained)  # True
print(index.ntotal)   # 20000

nprobe = 2  # find 2 most similar clusters
n_query = 1000
k = 30  # return 30 nearest neighbours
np.random.seed(0)
query_vectors = np.random.random((n_query, dimension)).astype('float32')
distances, indices = index.search(query_vectors, k)
print("distances:")
print(distances)
print("indices:")
print(indices)
