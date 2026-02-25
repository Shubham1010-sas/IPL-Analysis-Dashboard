import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('matches.csv')

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# ── Chart 1: Total Matches Per Season ──
plt.figure()
season_counts = df['Season'].value_counts().sort_index()
sns.barplot(x=season_counts.index, y=season_counts.values, palette='Blues_d')
plt.title('Total Matches Per Season', fontsize=16)
plt.xlabel('Season')
plt.ylabel('Number of Matches')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('chart1_matches_per_season.png')
plt.show()

# ── Chart 2: Top 10 Winning Teams ──
plt.figure()
top_teams = df['winner'].value_counts().head(10)
sns.barplot(x=top_teams.values, y=top_teams.index, palette='Reds_r')
plt.title('Top 10 Winning Teams', fontsize=16)
plt.xlabel('Total Wins')
plt.ylabel('Team')
plt.tight_layout()
plt.savefig('chart2_top_winning_teams.png')
plt.show()

# ── Chart 3: Toss Decision Trend Over Years ──
plt.figure()
toss = df.groupby(['Season', 'toss_decision']).size().unstack()
toss.plot(kind='bar', color=['#f4a261', '#2a9d8f'])
plt.title('Toss Decision Trend Over Seasons', fontsize=16)
plt.xlabel('Season')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.legend(title='Decision')
plt.tight_layout()
plt.savefig('chart3_toss_decision_trend.png')
plt.show()

# ── Chart 4: Did Toss Winner Win the Match? ──
plt.figure()
df['toss_match_winner'] = df['toss_winner'] == df['winner']
toss_win = df['toss_match_winner'].value_counts()
plt.pie(toss_win.values, labels=['Toss Winner Won', 'Toss Winner Lost'],
        autopct='%1.1f%%', colors=['#e9c46a', '#264653'], startangle=90)
plt.title('Did Toss Winner Win the Match?', fontsize=16)
plt.tight_layout()
plt.savefig('chart4_toss_impact.png')
plt.show()

# ── Chart 5: Top 10 Player of the Match ──
plt.figure()
top_players = df['player_of_match'].value_counts().head(10)
sns.barplot(x=top_players.values, y=top_players.index, palette='Purples_r')
plt.title('Top 10 Player of the Match Awards', fontsize=16)
plt.xlabel('Awards')
plt.ylabel('Player')
plt.tight_layout()
plt.savefig('chart5_top_players.png')
plt.show()

print("✅ All 5 charts saved successfully!")