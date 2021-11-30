const form = document.forms[0]; // documentの最初のフォーム

form.addEventListener('submit', (e) => {
    const id = document.getElementById('id').value; // idの入力値を取得する
    const tel = document.getElementById('telephone').value; // 電話番号の入力値を取得する

    const id_error = document.getElementById('id_error'); // idのエラーメッセージを表示させる場所
    const tel_error = document.getElementById('tel_error'); // telのエラーメッセージを表示させる場所

    const regexInt = /^[1-9][0-9]*$/; // regex 数字の1以上
    const regexTel = /\d{2,4}-\d{2,4}-\d{2,4}$/; //数字（2〜4桁）-数字（2〜4桁）-数字（2〜4桁）

    const error_msg_id = '半角数字のみ、最大6桁です。';
    const error_msg_tel = '電話番号は「数字-数字-数字」です。';

    e.preventDefault(); // フォームの送信を停止する

    if (!(id.match(regexInt)) || !(id.length <= 6)) {
        return id_error.textContent = error_msg_id;
    } else if (!tel.match(regexTel)) {
        return tel_error.textContent = error_msg_tel;
    } else {
        form.submit(); // 入力値に問題がなければ送信
    }
}, false);
