# angstrom-python
Angstrom oefenmiddag met Python

## Wat gaan we doen?
In de datafiles [easy](easy_data.txt) en [ugly](ugly_data.txt) zit een Gaussisch verband verborgen. Wat zijn de parameters van de functie?

## Inlezen van de data
In volgorde van makkelijk (weinig opties) naar moeilijk (veel opties):
* numpy.loadtxt
* numpy.genfromtxt
* pandas.read_csv

## Weergave van de data
Eerste plot om de data te zien. Wat is de piekwaarde? Bij welke x-waarde is de piek? Wat is de breedte van de Gauss? Plot een eerste gok samen met de data. Heb je alle data nodig of kan je met een slice de dataset verkleinen?
* matplotlib.pyplot

### Wanneer beschrijft de functie de data?
Hoe ziet de data eruit als je de functie er vanaf trekt (residu)? Is er alleen maar ruis over?

## Datafitten
Is je eerste gok een juiste? Optimalisatie routines kunnen nu helpen:
* scipy.optimize.curve_fit
* leastsquares

### Wat zijn de eerste gokken?
Begin met je eigen gok. Na eerste fit uitkomst als begin-parameters gebruiken.

### Weergave van data met datafit en residu
Subplots om figuren bij elkaar te houden. 
* Hoe worden de assen opgemaakt? 
* Wat geef je weer? 
* Wat is de onzekerheid in de datafit? 
* Hoe goed past je model?

## Herhaling
Hoe geautomatiseerd honderden datasets inlezen. Hoe schrijf je ze weg met beschrijvende informatie (filenaam, textdocument)?

# Links
* [matplotlib](https://matplotlib.org/)
  + [voorbeelden](https://matplotlib.org/gallery/index.html)
  + [handleidingen](https://matplotlib.org/tutorials/index.html)
* [pandas](https://pandas.pydata.org/)
  + [10 minuten introductie](http://pandas.pydata.org/pandas-docs/stable/10min.html)
  + [Kookboek](http://pandas.pydata.org/pandas-docs/stable/cookbook.html)
  + [handleidingen](http://pandas.pydata.org/pandas-docs/stable/tutorials.html)
* [numpy](http://www.numpy.org/)
  + [handleiding](https://docs.scipy.org/doc/numpy-dev/user/quickstart.html)
* [Sympy - symbolisch rekenen](http://www.sympy.org/en/index.html)
  + [Live](http://live.sympy.org/)
  + [Gamma](http://gamma.sympy.org/)

Met jupyter is het mogelijk in de browser in Python te werken!
* [jupyter](http://jupyter.org/)
  + [speelruimte](https://nbviewer.jupyter.org/)
  + [Sympy in de browser](https://nbviewer.jupyter.org/github/ipython/ipython/blob/4.0.x/examples/IPython%20Kernel/SymPy.ipynb)

Git voor versiebeheer!
* [Github - account registratie](https://education.github.com/pack)
  + [Angstrom](https://github.com/Studievereniging-Angstrom)
  + [Docenten TN](https://hhs-tn.github.io/)


