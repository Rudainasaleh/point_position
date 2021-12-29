# point_position
The program askes the user to enter the coordinate of p0 and p1 points that creats a line 
and then askes for the coordinate of the p2 point thar the program see the place of the pont if its in the lift of the line, in right, or in the line.
  for the point p0 the coordinates (x0, y0) 
  for the point p1 the coordinates (x1, y1)
  for the point p2 the coordinates (x2, y2)
  
# if p2 is on the left of the line:
        (x1 – y0)  ́ (y2 – y0) – (x2 – x0)  ́ (y1 – y0) > 0
        
# if p2 is on the right of the line :
        (x1 – y0)  ́ (y2 – y0) – (x2 – x0)  ́ (y1 – y0) < 0
        
# if p2 is on the same line :
        (x1 – y0)  ́ (y2 – y0) – (x2 – x0)  ́ (y1 – y0) = 0
