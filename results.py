import matplotlib.pyplot as plt
import json

with open("ans_classes.json") as f:
   ans_classes = json.load(f)

ans_classes={k: v for k, v in sorted(ans_classes.items(), key=lambda item: item[1], reverse=True)}

with open("ques_classes.json") as f:
   ques_classes = json.load(f)

ques_classes={k: v for k, v in sorted(ques_classes.items(), key=lambda item: item[1], reverse=True)}

a_scores=list(ans_classes.values())
a_types=list(ans_classes.keys())

q_scores=list(ques_classes.values())
q_types=list(ques_classes.keys())

plt.figure()
plt.style.use('seaborn-darkgrid')  
plt.bar(a_types,a_scores,tick_label=a_types, color="palegreen", edgecolor="green", alpha=0.8)
plt.ylabel("Score")
plt.title("Scores per answer type")
plt.savefig("scores_per_anstype")

plt.figure(figsize=(12,15))
plt.style.use('seaborn-darkgrid')  
plt.bar(q_types,q_scores,tick_label=q_types, color="lightcoral")
plt.ylabel("Score", fontsize=9)
plt.xticks(rotation = 90, fontsize=9)
plt.title("Scores per question type",fontsize=14)
plt.savefig("scores_per_questiontype")