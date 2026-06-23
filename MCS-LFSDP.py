# ============================================================
# MCS-LFSDP: Simple Python-style Pseudocode
# Mechanism-Coupled Spectral Label-Free Software Defect Prediction
# ============================================================

def mcs_lfsdp(X, metric_names, effort=None):
    """
    X            : unlabeled target-project metric matrix
    metric_names : names of metrics in X
    effort       : optional inspection-effort vector

    Returns:
        risk_score        : label-free defect-risk score
        inspection_score  : effort-aware inspection score
        predicted_labels  : label-free binary predictions
        explanations      : mechanism-level explanation profile
    """

    # --------------------------------------------------------
    # 1. Preprocess target-project metrics
    # --------------------------------------------------------
    X = preprocess_metrics(X)

    # --------------------------------------------------------
    # 2. Build software-engineering mechanism views
    # --------------------------------------------------------
    mechanism_views = build_mechanism_views(
        X,
        metric_names,
        views=["Structural Burden",
               "Evolutionary Instability",
               "Coordination Complexity",
               "Dependency Exposure"]
    )

    active_views = select_available_views(mechanism_views)

    # --------------------------------------------------------
    # 3. Learn label-free risk evidence in each mechanism view
    # --------------------------------------------------------
    mechanism_scores = {}
    mechanism_graphs = {}

    for view_name, X_view in active_views.items():

        detector_outputs = compute_label_free_detectors(X_view)

        detector_weights = estimate_detector_reliability(
            detector_outputs
        )

        mechanism_scores[view_name] = combine_detector_outputs(
            detector_outputs,
            detector_weights
        )

        mechanism_graphs[view_name] = build_local_similarity_graph(
            X_view
        )

    # --------------------------------------------------------
    # 4. Estimate mechanism reliability
    # --------------------------------------------------------
    mechanism_weights = estimate_mechanism_reliability(
        mechanism_scores
    )

    # --------------------------------------------------------
    # 5. Couple mechanism evidence
    # --------------------------------------------------------
    base_risk_score = combine_mechanism_evidence(
        mechanism_scores,
        mechanism_weights
    )

    coupled_risk_score = apply_mechanism_coupling(
        base_risk_score,
        mechanism_scores
    )

    # --------------------------------------------------------
    # 6. Build mechanism-coherent graph
    # --------------------------------------------------------
    mechanism_graph = fuse_mechanism_graphs(
        mechanism_graphs,
        mechanism_weights
    )

    # --------------------------------------------------------
    # 7. Discover risky and safe anchors without labels
    # --------------------------------------------------------
    risky_anchors, safe_anchors = discover_label_free_anchors(
        coupled_risk_score
    )

    # --------------------------------------------------------
    # 8. Propagate anchor evidence with guarded refinement
    # --------------------------------------------------------
    propagated_score = guarded_graph_propagation(
        mechanism_graph,
        risky_anchors,
        safe_anchors
    )

    # --------------------------------------------------------
    # 9. Produce final defect-risk score
    # --------------------------------------------------------
    risk_score = combine_scores(
        coupled_risk_score,
        propagated_score
    )

    # --------------------------------------------------------
    # 10. Compute effort-aware inspection score
    # --------------------------------------------------------
    if effort is not None:
        inspection_score = compute_effort_aware_score(
            risk_score,
            effort
        )
    else:
        inspection_score = risk_score

    # --------------------------------------------------------
    # 11. Estimate label-free threshold and predict labels
    # --------------------------------------------------------
    threshold = estimate_label_free_threshold(
        risk_score,
        risky_anchors,
        safe_anchors
    )

    predicted_labels = assign_binary_labels(
        risk_score,
        threshold
    )

    # --------------------------------------------------------
    # 12. Generate mechanism-level explanations
    # --------------------------------------------------------
    explanations = explain_prioritized_modules(
        mechanism_scores,
        mechanism_weights,
        risk_score
    )

    return risk_score, inspection_score, predicted_labels, explanations


# ------------------------------------------------------------
# Note:
# Defect labels are not used in any step above.
# Labels are used only after prediction for evaluation.
# ------------------------------------------------------------
