# Create PAX packages for PUT Tool

The code is looking for a structure where each folder in the given parent folder refers to the lowest level CALM record, and each of those folders contain mxed access and preservation copies to be sorted

Example: Defining SB1 as the top directory

SB1/
  SB1-1/
    SB-1-001.tif
    SB-1-001.jpg
    SB-1-002.tif
    SB-1-002.jpg
  SB1-2/
    SB-2-001.tif
    SB-2-001.jpg
    SB-2-002.tif
    SB-2-002.jpg
 etc...

Would become

SB1/
  SB1-1/
    SB1-1-001.pax/
      Representation_Preservation/
            SB-1-001.tif
      Representation_Access/
            SB-1-001.jpg
    SB1-1-002.pax/
      Representation_Preservation/
            SB-1-002.tif
      Representation_Access/
            SB-1-002.jpg
  SB1-2/
    SB1-2-001.pax/
      Representation_Preservation/
            SB-2-001.tif
      Representation_Access/
            SB-2-001.jpg
    SB1-2-002.pax/
      Representation_Preservation/
            SB-2-002.tif
      Representation_Access/
            SB-2-002.jpg


# Editing the config file


