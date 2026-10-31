import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

grade_df = pd.read_excel('./final_grades.xlsx')
major_names = grade_df['Major'].unique()
print(major_names)
it_major = ['khmt', 'cntt', 'ttql']
it_students_df = grade_df[grade_df['Major'].isin(it_major)]
print(f'#IT students/#Total: {len(it_students_df)}/{len(grade_df)}')

grade_df['Result'] = grade_df['Grade'].apply(lambda x: 'Pass' if x>=5 else 'Fail')
grade_df['MajorGroup'] = grade_df['Major'].apply(lambda x: 'IT' if x in it_major else 'Non-IT')
print(grade_df.head())

it_students_df = grade_df[grade_df['MajorGroup'] == 'IT' ] 
print(it_students_df.head())

grade_df.to_csv('./final_grades_update.csv', index=False)

total_students = len(grade_df)
print(f'Total students: {total_students}')
mean_grade = grade_df['Grade'].mean()
print(f'Mean grade: {mean_grade:.2f}')
median_grade = grade_df['Grade'].median()
print(f'Median grade: {median_grade:.2f}')
std = grade_df['Grade'].std()
print(f'std grade: {std:.2f}')
min_grade = grade_df['Grade'].min()
print(f'Minimum grade: {min_grade:.2f}')
max_grade = grade_df['Grade'].max()
print(f'Maximum grade: {max_grade:.2f}')

# bins = np.arange(0, 10.5, 0.5)
# plt.figure(figsize=(10, 6))
# counts, edges, patches = plt.hist(grade_df['Grade'], bins=bins, edgecolor='white', alpha=0.7)

# for count, edge_left, edge_right in zip(counts, edges[:-1], edges[1:]):
#     if count > 0:  # only add text for bars with count > 0
#         # calculate the position for the text
#         x_pos = (edge_left + edge_right) / 2
#         y_pos = count + 0.5  # position the text slightly above the bar
#         # print the count value on top of the bar
#         plt.text(x_pos, y_pos, str(int(count)), 
#         ha='center',
#         va='bottom',
#         fontsize=10,
#         fontweight='bold',
#         color='black')

# stats_text = "{}{}\n{}{:.2f}\n{}{:.2f} \
# \n{}{:.2f}\n{}{:.2f}\n{}{:.2f}".format("Số bài thi: ", total_students,
#                                                     "Điểm trung bình: ", mean_grade,
#                                                     "Điểm trung vị: ",  median_grade,
#                                                     "Độ lệch chuẩn: ",std,
#                                                     "Điểm thấp nhất: ",min_grade,
#                                                     "Điểm cao nhất: " ,max_grade )

# plt.gca().text(
#     0.02, 0.95, stats_text,
#     transform=plt.gca().transAxes,
#     fontsize=11,
#     verticalalignment='top',
#     horizontalalignment='left',
#     bbox=dict(boxstyle='round', facecolor='white', alpha=0.6)
# )


# bin_interval = 0.5
# bins = np.arange(0, 10 + bin_interval, bin_interval)
# bin_labels = [str(bins[i]) + '-' + str(bins[i+1]) for i in range(len(bins)-1)]

# # Customize the chart
# plt.title("Thổng kê điểm thi môn Tin học đại cương A - HK2 2025-2026", fontsize=14, weight='bold')
# plt.xlabel("Điểm", fontsize=12)
# plt.ylabel("Số sinh viên", fontsize=12)
# # plt.xticks(bin_labels, rotation=90)
# plt.xticks(bins)
# plt.grid(axis='y', linestyle='--', alpha=0.1)

# # Display the plot 
# # plt.tight_layout()
# plt.savefig('THDC-Grade-Stats.png') 
# plt.show()

# Filter grades of IT group
grades_cntt = grade_df[grade_df['MajorGroup'] == 'IT']
# Filter grades of Non-IT group
grades_others = grade_df[grade_df['MajorGroup'] == 'Non-IT']

data1 = grades_cntt['Grade'].values
data2 = grades_others['Grade'].values

plt.figure(figsize=(9, 5))
bins = np.arange(0, 10 + 0.25, 0.5)
combined_data = np.hstack((data1, data2))
counts, bins = np.histogram(combined_data, bins=bins) # grade interval = 0.5

# Plot the histograms using the same bins
plt.hist([data1, data2], stacked=True, bins=bins, alpha=0.9, 
         label=['Nhóm ngành CNTT','Ngành khác'], color=['#ea801c', '#0099cc'], edgecolor='white')

# Compute basic statistics
# IT major
total_students_it = len(grades_cntt)
mean_grade_it = grades_cntt['Grade'].mean()
median_grade_it = grades_cntt['Grade'].median()
std_it = grades_cntt['Grade'].std()
min_grade_it = grades_cntt['Grade'].min()
max_grade_it = grades_cntt['Grade'].max()

# Non IT major
total_students_others = len(grades_others)
mean_grade_others = grades_others['Grade'].mean()
median_grade_others = grades_others['Grade'].median()
std_others = grades_others['Grade'].std()
min_grade_others = grades_others['Grade'].min()
max_grade_others = grades_others['Grade'].max()

# Annotate statistics at top-left 
stats_text = "{}{}/{}\n{}{:.2f}/{:.2f}\n{}{:.2f}/{:.2f} \
\n{}{:.2f}/{:.2f}\n{}{:.2f}/{:.2f}\n{}{:.2f}/{:.2f}".format("Số bài thi: ", total_students_it, total_students_others,
                                                    "Điểm trung bình: ", mean_grade_it, mean_grade_others,
                                                    "Điểm trung vị: ",  median_grade_it, median_grade_others,
                                                    "Độ lệch chuẩn: ",std_it, std_others,
                                                    "Điểm thấp nhất: ",min_grade_it, min_grade_others,
                                                    "Điểm cao nhất: " ,max_grade_it, max_grade_others)
plt.gca().text(
    0.02, 0.95, stats_text,
    transform=plt.gca().transAxes,
    fontsize=11,
    verticalalignment='top',
    horizontalalignment='left',
    bbox=dict(boxstyle='round', facecolor='white', alpha=0.6)
)

plt.xlabel('Mức điểm')
plt.ylabel('Số SV')
plt.title('So sánh phổ điểm giữa kỳ nhóm ngành CNTT và các ngành khác')
plt.xticks(bins)
plt.legend()
#plt.grid(True, linestyle='--', alpha=0.7)
plt.grid(axis='y', linestyle='--', alpha=0.1)
plt.legend(loc='center left')
# Save the chart to file
plt.savefig('grade-by-major.pdf')
# Show the plot
plt.show()