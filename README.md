# Reuse your SDXL captioning into pixart captioning by merging both natural language captioning and tagging

This script will merge your .txt file and .caption file that used in your SDXL datasets captioning architecture

# How to use
Run with command prompt by typing
`python merge_texts.py -s /path/to/source -d /path/to/destination`

`-s` is the path of your .caption and .txt source located
`-d` is destination where your merged .caption and .txt is outputed

For example
`python "G:\MergeText.py" -s "G:\AlphaTemp\Merged_Caption" -d "G:\AlphaTemp\Output"`

# How this script is works and how relevant to pixart captioning mechanism?
Based on the discussion in OneTrainer discord "the captions are chosen randomly. so even if you set it to 2, it might only train on one of them for some images" by Nerogar (OneTrainer Dev). So my conclusion is the merged captioning file should be seperated with new line.

For example:
1212121.txt containing:
``1girl, absurdres, antenna hair, bangs, bare shoulders, blush, breasts, collarbone, commentary request, doconim, eyebrows visible through hair, flower, grey background, hair between eyes, hair flower, hair ornament, highres, kokkoro (princess connect!), looking at viewer, medium breasts, pointy ears, princess connect!, princess connect! re dive, short hair, silver hair, simple background, smile, solo, violet eyes, white flower``

1212121.caption containing:
``A young girl with white hair, purple eyes, and fair complexion. She wearing green dress gold necklace. smiling has flower in her hair. camera angle close-up, capturing facial expression outfit details. scene appears to be set dark environment, the being main focus of image``

So the merged file looks like:
``` [1] 1girl, absurdres, antenna hair, bangs, bare shoulders, blush, breasts, collarbone, commentary request, doconim, eyebrows visible through hair, flower, grey background, hair between eyes, hair flower, hair ornament, highres, kokkoro (princess connect!), looking at viewer, medium breasts, pointy ears, princess connect!, princess connect! re dive, short hair, silver hair, simple background, smile, solo, violet eyes, white flower```

``` [2] A young girl with white hair, purple eyes, and fair complexion. She wearing green dress gold necklace. smiling has flower in her hair. camera angle close-up, capturing facial expression outfit details. scene appears to be set dark environment, the being main focus of image```

# Requirements:
Any version of python
