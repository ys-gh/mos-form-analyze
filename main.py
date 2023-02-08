from firebase_admin import firestore
import numpy as np


def main():

    db = firestore.Client()
    methods = ["m1", "m2", "m3"]

    for method in methods:
        all_subject_scores = []
        docs = db.collection(method).stream()
        num_subject = 0

        for doc in docs:
            doc = doc.to_dict()
            scores = [int(i) for i in list(doc.values())]

            all_subject_scores += scores
            num_subject += 1

        mos = np.mean(all_subject_scores)
        # print(len(all_subject_scores))
        ci = 1.96 * np.std(all_subject_scores, ddof=1) / np.sqrt(len(all_subject_scores))
        print(f"method: {method} MOS: {mos} +- {ci}")

    print(f"number of subjects: {num_subject}")


if __name__ == '__main__':
    main()
