<?php

function distance($a, $b)
{
    $a_length = strlen($a);
    $b_length = strlen($b);

    $count = 0;

    if ($a_length === $b_length) {
      for ($i = 0; $i < $a_length; $i++) {
        if ($a[$i] !== $b[$i]) {
          $count += 1;
        }
      }
    } else {
      throw new InvalidArgumentException("DNA strands must be of equal length.");
    }

    return $count;
}
