<?php

require "gigasecond.php";

class GigasecondTest extends \PHPUnit_Framework_TestCase
{

    public function dateSetup($date)
    {
        $UTC = new DateTimeZone("UTC");
        $date = new DateTime($date, $UTC);
        return $date;
    }

    public function test1()
    {
        $date = GigasecondTest::dateSetup("2011-04-25");
        $gs = from($date);

        $this->assertSame("2043-01-01 01:46:40", $gs->format("Y-m-d H:i:s"));
    }

    public function test2()
    {
        $date = GigasecondTest::dateSetup("1977-06-13");
        $gs = from($date);

        $this->assertSame("2009-02-19 01:46:40", $gs->format("Y-m-d H:i:s"));
    }

    public function test3()
    {
        $date = GigasecondTest::dateSetup("1959-7-19");
        $gs = from($date);

        $this->assertSame("1991-03-27 01:46:40", $gs->format("Y-m-d H:i:s"));
    }

    public function test4()
    {
        $date = GigasecondTest::dateSetup("2015-01-24 22:00:00");
        $gs = from($date);

        $this->assertSame("2046-10-02 23:46:40", $gs->format("Y-m-d H:i:s"));
    }

    public function test5()
    {
        $date = GigasecondTest::dateSetup("2015-01-24 23:59:59");
        $gs = from($date);

        $this->assertSame("2046-10-03 01:46:39", $gs->format("Y-m-d H:i:s"));
    }

    public function testYourself()
    {
        $your_birthday = GigasecondTest::dateSetup("1985-03-26 04:00:00");
        $gs = from($your_birthday);

        $this->assertSame("2016-12-02 05:46:40", $gs->format("Y-m-d H:i:s"));
    }
}
