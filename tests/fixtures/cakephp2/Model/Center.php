<?php

class Center extends AppModel
{
    public $name = 'Center';

    public $hasMany = [
        'User'
    ];

    public function getCenters()
    {
        return $this->find('all');
    }

    public function saveCenter($data)
    {
        return $this->save($data);
    }
}