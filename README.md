# NarrativeChart
Design team homogenity at closing RFIs

# Background

This narrative chart captures the critical RFI completion phase during the latter end of a data centre construction project in Denmark. Prompted by the client, my company's upper management wanted a succinct method to track the fourteen individual design teams in the project. This team consisted of over fifty colleagues, mostly based in Ireland, and the UK. 

I've taken inspiration from Randall Munroe's more iconic xkcd strips, which visualises the timelines of several films in narrative charts. An example of this can be an input a list of character names, followed by a list of events. Each event is either a list of dying characters, or a list of groups of characters (signifying which characters are currently together). 

![image](https://user-images.githubusercontent.com/86113858/129120193-fb662645-7707-4d12-9d77-4b7c93afa2fe.png)

Exchanging character names, denoted as "chars", with the design teams in my project, and events to their RFI closure progress:

```
chars = ["Electrical","Structural","Civil","Mechanical","HVAC","Controls","Plumbing",
        "Concrete Pour","Rebar","Generator","Safety","Roads","Trestles","Misc."
]
events =[
        [[0,1,2,3,4,5,6,7,8,10,11,12,9,13]],
        [[0,1,2,3],[4,7,5],[6,8,9,10],[11,12],[13]],
        [[0,1,2,3],[4,7,5,6,8],[9,10],[11,12],[13]],
        [[0],[1,2,3],[4,7],[5,6,9],[8,10,11,12],[13]],
        [[0,4,7],[1,2,3],[5,9],[6,8,10,11],[12],[13]],
        [4],
        [[5,9],[0,7,6,10],[1,2,3],[8,11],[12,13]],
        [12],
        [[0,5,9],[1,2],[3],[7,6,10,8,11],[13]],
        [[0],[5,9],[1,2],[3,11],[7,6,10,8],[13]],
        [11],
        [[0],[5,9],[1,2,10],[3,6],[7,8],[13]],
        [5],
        [6],
        [[0],[10,1,2,9],[3],[7,8],[13]],
        [7],
        [[0],[10,1,9],[3,8],[2],[13]],
        [8],
        [[0,1,10],[9,3],[2],[13]],
        [9],
        [1],
        [3],
        [[0],[2],[13]]
]
```

In the first line at the very top, all fourteen design teams are together with outstanding RFI tasks of roughly the same number. In this case, the same location on the y-axis entitled "Design Team homogenity at closing RFIs". In the second line, the teams become isolated from one another, as the quantity of their RFIs change from the other teams, ie. the electrical, structural, civil and mechanical teams start from the other teams. In the sixth line, the HVAC team are isolated, and thus die off from the chart, as they've completed the outstanding RFIs. The same logic continues throughout the rest of the events. 

In this narrative chart, the quantity doesn't matter, as we want to show the stochastic nature of how the different groups of design teams close the outstanding RFIs. The fourteen lines follow a similar pattern as with the Second Law of Thermodynamics, which says, in simple terms, entropy always increases. In other words, a system becomes more and more random over time, and doesn't get simpler. The same can be applied to Randall Munroe's xkcd strips, and the storyline of the Lord of the Rings. This was to much amusement of my colleagues, many of whom were J. R. R. Tolkien fans. It was an added bonus, to bring much needed cohesion to a much needed project, and avoided the teams from having to look at yet another bland excel template.  

At the end of a period of twelve weeks, ten design teams had successfully closed their RFIs, denoted on the chart by a large full stop on the respective line. A 75% success rate. Three teams still hadn't completed their task, and this was escalated to internal upper management, who dealt with the matter. 

This was the final result:

![image](https://user-images.githubusercontent.com/86113858/129119548-fb3e8e6d-506b-4cca-ab3a-8910891bd383.png)


