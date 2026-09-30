"""Completed pandas foundations demonstration for STAT 386."""

from pathlib import Path

import pandas as pd


DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "talks.csv"


def build_recent_talks(talks: pd.DataFrame) -> pd.DataFrame:
    """Select the columns used in class for talks from 2018 through 2020."""
    recent_mask = talks["year"].between(2018, 2020)
    columns = ["talk_name", "speaker", "conference", "year", "num_words"]
    return talks.loc[recent_mask, columns].copy()


def answer_final_request(talks: pd.DataFrame) -> pd.DataFrame:
    """Build the ordered result used in the final activity."""
    request_mask = (
        talks["year"].between(2019, 2020)
        & (talks["session"] == "sunday-morning")
        & talks["num_words"].between(1400, 1700)
    )

    selected = talks.loc[
        request_mask,
        ["talk_name", "speaker", "conference", "year", "num_words"],
    ]

    return selected.sort_values(
        ["year", "num_words"],
        ascending=[False, False],
    )


def main() -> None:
    talks = pd.read_csv(DATA_PATH)

    print("Complete dataset")
    print(f"Shape: {talks.shape}")
    print()

    recent_talks = build_recent_talks(talks)
    print("Five largest word counts from 2018 through 2020")
    print(
        recent_talks.sort_values("num_words", ascending=False)
        .head(5)
        .to_string(index=False)
    )
    print()

    result = answer_final_request(talks)
    print("Final activity result")
    print(result.to_string(index=False))

    assert talks.shape == (794, 14)
    assert recent_talks.shape == (201, 5)
    assert len(result) == 6
    assert result["year"].isin([2019, 2020]).all()
    assert result["num_words"].between(1400, 1700).all()
    assert talks.loc[result.index, "session"].eq("sunday-morning").all()


if __name__ == "__main__":
    main()

