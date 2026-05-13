def classificar_estado_controle(pns_index, rmssd, sns_index, stress_index):

    score_estresse = 0
    score_calmaria = 0
    score_flow = 0

    # ESTRESSE
    if pns_index <= -0.5:
        score_estresse += 2
    if rmssd < 25:
        score_estresse += 2
    if sns_index >= 1:
        score_estresse += 1
    if stress_index > 40:
        score_estresse += 1

    # CALMARIA
    if pns_index > -0.2:
        score_calmaria += 2
    if rmssd > 40:
        score_calmaria += 2
    if sns_index < 0.5:
        score_calmaria += 1
    if stress_index < 30:
        score_calmaria += 1

    # FLOW
    if -0.5 <= pns_index <= 1.5:
        score_flow += 2
    if 25 <= rmssd <= 70:
        score_flow += 2
    if 0 <= sns_index <= 1.5:
        score_flow += 2
    if 25 <= stress_index <= 40:
        score_flow += 1

    scores = {
        "ESTRESSE": score_estresse,
        "CALMARIA": score_calmaria,
        "FLOW": score_flow
    }

    max_score = max(scores.values())
    estados_maximos = [k for k, v in scores.items() if v == max_score]

    if len(estados_maximos) > 1:
        if "FLOW" in estados_maximos:
            return "FLOW"
        return "INDEFINIDO"

    return estados_maximos[0]


estado = classificar_estado_controle(
    pns_index=-0.15,
    rmssd=5,
    sns_index=3.62,     
    stress_index=38    
)

print("Estado emocional dessa fase é:", estado)
