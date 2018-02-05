var jenkonsul = {

    colorize: function(nTd, sData, oData, iRow, iCol) {

                    // Set the color of cell
                    if(sData == 'FAILURE')
                    {
                      $(nTd).css('backgroundColor', 'red');
                      $(nTd).css('color', 'white');
                    }
                    if(sData == 'SUCCESS')
                    {
                      $(nTd).css('backgroundColor', 'green');
                      $(nTd).css('color', 'white');
                    }
                    else {
                      // Default is no color
                    }
    },

    buildNumberLink: function(nTd, sData, oData, iRow, iCol) {
        $(nTd).html("<a href='"+oData.url+"'>Build #"+sData+"</a>");
    },

    urlLink: function(nTd, sData, oData, iRow, iCol) {
        $(nTd).html("<a href='"+sData+"'>URL</a>");
    },

    claimLink: function(nTd, sData, oData, iRow, iCol) {

        // If job is FAILED, but not claimed add a link to the page where you can claim it
        if(oData.result == 'FAILURE' && oData.claim == null)
        {
            $(nTd).html("<a href='"+oData.url+"'>Claim</a>");
        }
    },

    formatTime: function (nTd, sData, oData, iRow, iCol) {
      $(nTd).html(sData.minutes + ":" + sData.seconds);
    },
};
