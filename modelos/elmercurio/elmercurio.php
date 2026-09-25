<?php

/**
 * Necessario passar a dia na variavel $dia
 */

$dia = 25;



function sendRequest($url, $postRequest=null , $headers=null, $cookies=null, $download=null){

    // Salvar cookies para usar depois
    $cookieJar =  __DIR__ ."/cookies_elmercurio.txt";
    $ch = curl_init($url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
    curl_setopt($ch, CURLOPT_MAXREDIRS, 10);

    if($download) {
        print_r($download);
        
        $fp = fopen($download, 'w+');
        curl_setopt($ch, CURLOPT_FILE, $fp);  
    }

    if($postRequest) {
        // echo "post\n\n";
        curl_setopt($ch, CURLOPT_POST, true);
        curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($postRequest));    
    }

    if($headers){
        //  echo "header\n\n";
        curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
        // curl_setopt($ch, CURLOPT_HEADER, true);
    }

    if($cookies) {
        //  echo "cooke\n\n";
        curl_setopt($ch, CURLOPT_COOKIE, $cookies);
        curl_setopt($ch, CURLOPT_COOKIEJAR, $cookieJar);
        curl_setopt($ch, CURLOPT_COOKIEFILE, $cookieJar);
    }
    curl_setopt($ch, CURLOPT_ENCODING, ''); 



    $result = curl_exec($ch);
    $info = curl_getinfo($ch);
    // print_r($info);
    return [$result, $ch ];
}



$url = "https://digital.elmercurio.com/Authenticate";
$postRequest = [
    'login'    => 'assinatura@fabricadeideias.com',
    'password' => 'F@brica2025',
    'action'   => 'appToken',
];

$headers = [
    "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:134.0) Gecko/20100101 Firefox/134.0",
    "Accept: text/plain, */*; q=0.01",
    "Accept-Language: pt-BR,es-ES;q=0.8,es;q=0.7,en-US;q=0.5,en;q=0.3,ast;q=0.2",
    "Accept-Encoding: gzip, deflate, br, zstd",
    "Content-Type: application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With: XMLHttpRequest",
    "Origin: https://digital.elmercurio.com",
    "Referer: https://digital.elmercurio.com",
    "Connection: keep-alive",
];
$token= "709p4r346245s6r7882p5rsp7p181rn37os1o4o04r6q7pq0r0p40p69ss16n1q2";
$cookies = "_pk_ref.3.a4f6=%5B%22%22%2C%22%22%2C1762884999%2C%22https%3A%2F%2Fatendimento.empauta.com%2F%22%5D; ".
           "_pk_id.3.a4f6=4f9d5c04d9adaaa4.1753103356.6.1762885005.1762876460.; ".
           "T=".$token."; ".
           "_pk_ses.3.a4f6=1; ".
           "LastUrlBeforeAuth=https://digital.elmercurio.com/2025/11/06/A/8V4JGK3M#zoom=page-width";


$res = sendRequest($url, $postRequest, $headers, $cookies);
// ----------------------------------------
// ----------------------------------------
// ----------------------------------------
$arrayEdicao = [
    "A" => 'A',
    "B" => 'B',
    "C" => 'C',
    "E" => 'EE-TAB-J',
    "P" => 'P',
    "Q" => 'EMSU',
    "M" => 'ME-I',
];

foreach($arrayEdicao as $categoria => $slugCategoria){

    
    $url = "https://digital.elmercurio.com/2026/09/".$dia."/".$slugCategoria;
    echo "\n\n{$url}\n\n";
    $cookies = "_pk_ref.3.a4f6=%5B%22%22%2C%22%22%2C1762884999%2C%22https%3A%2F%2Fatendimento.empauta.com%2F%22%5D; ".
               "_pk_id.3.a4f6=4f9d5c04d9adaaa4.1753103356.6.1762885005.1762876460.; ".
               "T=".$res[0]."; ".
               "_pk_ses.3.a4f6=1; ".
               "LastUrlBeforeAuth=https://digital.elmercurio.com/2025/11/13/A/8V4JGK3M#zoom=page-width";
    $res2 = sendRequest($url, null, $headers, $cookies);
    
    $pg=1;
    
    $veiculo = "Elmercurio/".$dia.$categoria;
    $arquivo = $veiculo;
    exec("mkdir -p img/$arquivo");
    
    
    
    if(preg_match('#<div class="contBnewsMer" id="cont_all_bnews">(.*?)</section>#is', $res2[0], $contentDoDia)){
       
        if(preg_match_all("#(https://digital.elmercurio.com/\d{4}/\d+/\d+/content/pages/img/big/[\w\d-]+.jpg\?gt=\d+)#is", $contentDoDia[1], $links_big)){


            foreach($links_big[1] as $page_) {
                echo $page_.PHP_EOL;
                $download = "img/".$arquivo."/".$categoria."_".str_pad($pg, 4, '0', STR_PAD_LEFT).".jpg";
                sendRequest($page_, null, $headers, $cookies, $download);
                $pg++;
            
                sleep(1);
                
            }
        }else {
    echo "\nSem Edição ".$dia.$categoria."\n\n";
}
} else {
    echo "\nSem Edição ".$dia.$categoria."\n\n";
}
}
curl_close($res2[1]);