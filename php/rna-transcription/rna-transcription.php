<?php

function toRna($strand)
{
    return strtr($strand, 'GCTA', 'CGAU');
}
