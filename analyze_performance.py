from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = Path(__file__).with_name("students.csv")

def main():
    df = pd.read_csv(DATA_FILE)
    subjects = ["maths", "programming", "english"]
    df["total"] = df[subjects].sum(axis=1)
    df["average"] = df[subjects].mean(axis=1)

    print("Student performance summary")
    print("---------------------------")
    print(f"Students analysed: {len(df)}")
    print(f"Class average: {df['average'].mean():.2f}")
    print("\nTop 3 students by average:")
    print(df.nlargest(3, "average")[["name", "total", "average"]].to_string(index=False))

    subject_averages = df[subjects].mean()
    subject_averages.plot(kind="bar", title="Average Marks by Subject", xlabel="Subject", ylabel="Average mark")
    plt.tight_layout()
    output_file = Path(__file__).with_name("subject_averages.png")
    plt.savefig(output_file, dpi=150)
    print(f"\nChart saved to: {output_file.name}")
    plt.show()

if __name__ == "__main__":
    main()
