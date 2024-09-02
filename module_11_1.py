import pandas as pd

students = pd.read_csv("Students_Performance_132b1e1ff9.csv")  # В качестве примера взял учебный фаил из интернета

# Выбор 10 результатов тестов по математике
print(students[students["test preparation course"] == "completed"]["math score"].head(10))
print()

# Получение последних строк (по умолчанию 5)
print(students.tail(3))
print()

# Сортировка лучших результатов по 3 дисциплинам по убыванию
with_course = students[students["test preparation course"] == "completed"]
print(with_course[["math score",
                   "reading score",
                   "writing score"]].sort_values(["math score",
                                                  "reading score",
                                                  "writing score"], ascending=False).head(7))
print()

# Сортировка по сумме баллов с созданием дополнительного столбца
with_course = students[students["test preparation course"] == "completed"]
students["total score"] = students["math score"] + students["reading score"] + students["writing score"]
print(students.sort_values(["total score"], ascending=False).head())

# Группировка записи по признаку. Метод groupby() группирует, метод count() определяет количество сгруппированных данных
print(students.groupby(["gender", "test preparation course"])["writing score"].count())
