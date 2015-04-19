<?php

function toRna($strand)
{
    $transcription = '';
    for ($i = 0; $i < strlen($strand); $i++) {
        if ($strand[$i] === 'G') {
            $transcription .= 'C';
        } elseif ($strand[$i] === 'C') {
            $transcription .= 'G';
        } elseif ($strand[$i] === 'T') {
            $transcription .= 'A';
        } elseif ($strand[$i] === 'A') {
            $transcription .= 'U';
        } else {
            throw new UnexpectedValueException("$strand[$i] is an invalid nucleotide!");
        }
    }
    return $transcription;
}
