<?php

function from($date)
{
    $date = $date->add(new DateInterval('PT1000000000S'));
    return $date;
}
