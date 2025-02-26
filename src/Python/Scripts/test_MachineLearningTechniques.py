import MachineLearningTechniques as ML

# test_ml_native.py
def run_tests():
    tests = []
    X_reg = [[1], [2], [3]]
    y_reg = [2, 4, 6]
    X_clf = [[0], [1], [2], [3]]
    y_clf = [0, 0, 1, 1]
    X_cluster = [[1, 2], [1, 4], [4, 2], [4, 4]]
    chunk_x = list(range(7))
    chunk_y = list(range(10, 17))

    # Test Linear Model
    try:
        model = ML.LinearModel(X_reg, y_reg)
        prediction = model.predict([[4]])[0]
        assert abs(prediction - 8.0) < 0.1, "Linear model prediction failed"
        tests.append(("Linear Model Basic", True))
    except Exception as e:
        tests.append(("Linear Model Basic", False, str(e)))

    # Test Linear Model Parameters
    try:
        slope, intercept = ML.LinearModelParams(X_reg, y_reg)
        assert abs(slope[0] - 2.0) < 0.1, "Slope incorrect"
        assert abs(intercept - 0.0) < 0.1, "Intercept incorrect"
        tests.append(("Linear Model Parameters", True))
    except Exception as e:
        tests.append(("Linear Model Parameters", False, str(e)))

    # Test Shape Validation
    try:
        ML.LinearModel([[1], [2]], [1])
        tests.append(("Shape Validation", False, "No error raised"))
    except ValueError:
        tests.append(("Shape Validation", True))
    except Exception as e:
        tests.append(("Shape Validation", False, str(e)))

    # Test KMeans Clustering
    try:
        model = ML.KMeansModel(2, X_cluster)
        assert len(model.cluster_centers_) == 2, "Cluster count mismatch"
        tests.append(("KMeans Basic", True))
    except Exception as e:
        tests.append(("KMeans Basic", False, str(e)))

    # Test Logistic Regression
    try:
        model = ML.LogisticRegressionModel(X_clf, y_clf)
        prediction = model.predict([[1.5]])[0]
        assert prediction in [0, 1], "Invalid prediction"
        tests.append(("Logistic Regression", True))
    except Exception as e:
        tests.append(("Logistic Regression", False, str(e)))

    # Test Evaluation Metrics
    try:
        reg_model = ML.LinearModel(X_reg, y_reg)
        metrics = ML.evaluate_basic_metrics(reg_model, X_reg, y_reg)
        assert metrics['mean_squared_error'] < 0.1, "MSE too high"
        tests.append(("Regression Metrics", True))
    except Exception as e:
        tests.append(("Regression Metrics", False, str(e)))

    # Test Chunk Creation
    try:
        xc, yc = ML.make_chunks(chunk_x, chunk_y, 2)
        assert len(xc) == 3, "Chunk count mismatch"
        assert xc[0] == [0, 1], "X chunk content error"
        assert yc[0] == [12, 13], "Y chunk content error"
        tests.append(("Chunk Creation", True))
    except Exception as e:
        tests.append(("Chunk Creation", False, str(e)))

    # Test MAPE Calculation
    try:
        mape = ML.mean_absolute_percentage_error([100, 200], [110, 190])
        assert abs(mape - 7.5) < 1.0, "MAPE calculation error"
        tests.append(("MAPE Calculation", True))
    except Exception as e:
        tests.append(("MAPE Calculation", False, str(e)))

    # Print Results
    print("\nTest Results:")
    for name, status, *error in tests:
        if status:
            print(f"✓ {name}")
        else:
            print(f"✗ {name} - Error: {error[0] if error else 'Unknown'}")

    # Exit code based on results
    failures = sum(1 for t in tests if not t[1])
    if failures > 0:
        print(f"\n{failures}/{len(tests)} tests failed!")
        exit(1)
    else:
        print(f"\nAll {len(tests)} tests passed!")
        exit(0)

if __name__ == "__main__":
    run_tests()
