def build_condition(selections: dict[str, str]) -> str:
    return " / ".join(
        [
            selections["purpose"],
            selections["companion"],
            selections["mood"],
            selections["time"],
        ]
    )


def add_to_plan(
    plan: list[dict],
    recommendation: dict,
    selections: dict[str, str],
) -> list[dict]:
    if any(item["place"] == recommendation["place"] for item in plan):
        return plan

    item = {
        "place": recommendation["place"],
        "reason": recommendation["reason"],
        "tips": recommendation["tips"],
        "condition": build_condition(selections),
    }
    return [*plan, item]


def remove_from_plan(plan: list[dict], place: str) -> list[dict]:
    return [item for item in plan if item["place"] != place]
