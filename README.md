# PCS-Diagram
Easily create beautiful [pitch-class set](https://en.wikipedia.org/wiki/Set_theory_%28music%29) [diagrams](https://en.wikipedia.org/wiki/Chromatic_circle).  
  
The output format is pdf. As it's a vector format, there's no loss of quality. The diagram can be integrated into any document (Word, OpenOffice, LaTeX, etc.).

### Requirements
* [python3](https://www.python.org/downloads/)
* fpdf2 package
* PyPDF2 package

To install these packages, run: 

```
pip3 install fpdf2 pyPDF2
```

### Running
```
python3 PCS-Diagram.py
```

### Options

| **Color option** | **Resulting polygon** |
|:----------------:|:---------------------:|
|        red       |          fill         |
|      orange      |          fill         |
|      yellow      |          fill         |
|       green      |          fill         |
|       blue       |          fill         |
|      violet      |          fill         |
|       grey       |          fill         |
|       none       |         outline       |

### Examples
<img src="./screenshot1.jpg" width="200" /> <img src="./screenshot2.jpg" width="200" /> <img src="./screenshot3.jpg" width="200" />
