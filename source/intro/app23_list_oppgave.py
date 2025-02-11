'''
Oppgave:
Jeg har fått en file med shiptypes.txt som inneholder en liste av skipstyper.
Jeg skal bruke denne listen i et WPF prosjekt og lurer på hvordan jeg kan lage en ComboBoxItem for hver skipstype.
En compoboxItem ser slik ut:
<ComboBoxItem x:Name="skipstype" Content="skipstype" />
problemet er at noen skipstyper inneholder " ", "-", "/" og " " som jeg ikke kan ha i x:Name.

Eksempel fra filen:
..
Grab-fitted Supramax
..

men vi vil ha 
<ComboBoxItem x:Name="GrabfittedSupramax" Content="Grab-fitted Supramax" />

hint 
  Loop med: for val in list
  str.replace("b", "a")
  print(f'test {variabel} test')

'''
