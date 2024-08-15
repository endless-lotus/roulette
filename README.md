# roulette
Is a gambling game I created to be played fully in the terminal. It includes the common bet types that are allowed in an American roulette table. It consists of one class: Player.

<h2>Bet Types</h2>
<ul>
  <li>Red🔴 or Black⚫</li>
  <p>To bet on the opposing colors red or black and gives a payout of 1:1.</p>
  <li>Odd or Even</li>
  <p>Allows you to choose if the number will land on an odd or even number in the 36 numbers of roulette, a payout of 1:1.</p>
  <li>1 to 18 || 19 to 36</li>
  <p>Allows you to choose if the number will land on one half 1-18 or the other half 19-36, a payout of 1:1.</p>
  <li>Dozens</li>
  <p>There are 3 batches of 12 in 36 that you can choose to bet on, a payout of 2:1.</p>
</ul>

<h2>Terminal Art</h2>
<figure>
  <img src= "https://github.com/user-attachments/assets/ebc7b28b-7f17-4c1d-9ff6-cfac93ad83b2"><br>
  <figcaption>This is my roulette art of the betting table depicting the colors of the numbers and the types of bets in the terminal game. It's not exact to the American roulette board style but easier to learn for someone just trying out roulette for the first time.</figcaption>
</figure>
<br>
<figure>
  <img src= "https://github.com/user-attachments/assets/36ca1597-8b09-4b1b-91bc-c959016d4b1d"><br>
  <figcaption>The Roulette Wheel (Does not include all 36 spots just rough visualization). Its fun art to break between the bet dialogues in the terminal and the return.</figcaption>
</figure>

<h2>Problems I Encountered</h2>
This is my first project in python. Working with classes was a agreat experience also learning halfway through that global varaibles shared between classses are a Big Bad. I decided to take away my secondary class the Casino and see how well I could do with just one class. This mainly occured because I could not think of any ideas for what to use the Casino for especially when the Player class held all the information I needed to continue the game flow. This helped cement my foundational learnings of ranges.Towards the end I learned I should have made a game loop! To continue the game if self.balance > 0.
