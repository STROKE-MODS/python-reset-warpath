--Q1 Each Player's Name and Rank.
select p.Player_ID,p.Name,r.Rank_Name from Players as p
    join Ranks as r
    on p.Player_ID=r.Player_ID;

--Q2 Top scorer for each match the one with highest kills,
select p.Name,r.Kills from Players as p
    join Results as r
    on p.Player_ID=r.Player_ID
    where r.Kills= (select max(Kills) from Results)
    group by Match_ID;

--Q3 Show total kills made by each player across all matches.
select p.Name,r.Kills from Players as p
    join Results as r
    on p.Player_ID=r.Player_ID
    group by p.Player_ID;

--Q4 Show average kills per match for every player.
select p.Name,avg(case when r.Match_ID=1 then r.Kills end) as 'Match1',
    avg(case when r.Match_ID=2 then r.Kills end) as 'Match2',
    avg(case when r.Match_ID=3 then r.Kills end) as 'Match3'
    from Players as p
    join Results as r
    on p.Player_ID=r.Player_ID
    group by p.Player_ID;

