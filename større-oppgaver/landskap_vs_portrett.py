def landskap_vs_portrett(høyde, bredde):
    if høyde == bredde:
        return "Square"
    elif høyde >= bredde:
        return "Portrait"
    else:
        return "Landscape"
