'use strict';
const MANIFEST = 'flutter-app-manifest';
const TEMP = 'flutter-temp-cache';
const CACHE_NAME = 'flutter-app-cache';

const RESOURCES = {"assets/app/app.zip": "ad6f5e5b31a1f07c6b0505355c619b28",
"assets/app/app.zip.hash": "c3d8f374441ed9372afec88474fbf3d3",
"assets/AssetManifest.bin": "3cc047d935b3aa5936c0e5db72bcc757",
"assets/AssetManifest.bin.json": "d380973e2c4cc87890ae2c7e5db50c2f",
"assets/FontManifest.json": "9bd568e67ff3c6c597e4f9494ef71249",
"assets/fonts/MaterialIcons-Regular.otf": "f34ace52ea74c95e26949fab4870ac22",
"assets/fonts/roboto.woff2": "e507bd45228483ae2f864d36f26bb43e",
"assets/NOTICES": "9955a5d78e775bb9d7514698f560c860",
"assets/packages/cupertino_icons/assets/CupertinoIcons.ttf": "6323a28c4d27ae6070923bcb643dc985",
"assets/packages/flutter_math_fork/lib/katex_fonts/fonts/KaTeX_AMS-Regular.ttf": "657a5353a553777e270827bd1630e467",
"assets/packages/flutter_math_fork/lib/katex_fonts/fonts/KaTeX_Caligraphic-Bold.ttf": "a9c8e437146ef63fcd6fae7cf65ca859",
"assets/packages/flutter_math_fork/lib/katex_fonts/fonts/KaTeX_Caligraphic-Regular.ttf": "7ec92adfa4fe03eb8e9bfb60813df1fa",
"assets/packages/flutter_math_fork/lib/katex_fonts/fonts/KaTeX_Fraktur-Bold.ttf": "46b41c4de7a936d099575185a94855c4",
"assets/packages/flutter_math_fork/lib/katex_fonts/fonts/KaTeX_Fraktur-Regular.ttf": "dede6f2c7dad4402fa205644391b3a94",
"assets/packages/flutter_math_fork/lib/katex_fonts/fonts/KaTeX_Main-Bold.ttf": "9eef86c1f9efa78ab93d41a0551948f7",
"assets/packages/flutter_math_fork/lib/katex_fonts/fonts/KaTeX_Main-BoldItalic.ttf": "e3c361ea8d1c215805439ce0941a1c8d",
"assets/packages/flutter_math_fork/lib/katex_fonts/fonts/KaTeX_Main-Italic.ttf": "ac3b1882325add4f148f05db8cafd401",
"assets/packages/flutter_math_fork/lib/katex_fonts/fonts/KaTeX_Main-Regular.ttf": "5a5766c715ee765aa1398997643f1589",
"assets/packages/flutter_math_fork/lib/katex_fonts/fonts/KaTeX_Math-BoldItalic.ttf": "946a26954ab7fbd7ea78df07795a6cbc",
"assets/packages/flutter_math_fork/lib/katex_fonts/fonts/KaTeX_Math-Italic.ttf": "a7732ecb5840a15be39e1eda377bc21d",
"assets/packages/flutter_math_fork/lib/katex_fonts/fonts/KaTeX_SansSerif-Bold.ttf": "ad0a28f28f736cf4c121bcb0e719b88a",
"assets/packages/flutter_math_fork/lib/katex_fonts/fonts/KaTeX_SansSerif-Italic.ttf": "d89b80e7bdd57d238eeaa80ed9a1013a",
"assets/packages/flutter_math_fork/lib/katex_fonts/fonts/KaTeX_SansSerif-Regular.ttf": "b5f967ed9e4933f1c3165a12fe3436df",
"assets/packages/flutter_math_fork/lib/katex_fonts/fonts/KaTeX_Script-Regular.ttf": "55d2dcd4778875a53ff09320a85a5296",
"assets/packages/flutter_math_fork/lib/katex_fonts/fonts/KaTeX_Size1-Regular.ttf": "1e6a3368d660edc3a2fbbe72edfeaa85",
"assets/packages/flutter_math_fork/lib/katex_fonts/fonts/KaTeX_Size2-Regular.ttf": "959972785387fe35f7d47dbfb0385bc4",
"assets/packages/flutter_math_fork/lib/katex_fonts/fonts/KaTeX_Size3-Regular.ttf": "e87212c26bb86c21eb028aba2ac53ec3",
"assets/packages/flutter_math_fork/lib/katex_fonts/fonts/KaTeX_Size4-Regular.ttf": "85554307b465da7eb785fd3ce52ad282",
"assets/packages/flutter_math_fork/lib/katex_fonts/fonts/KaTeX_Typewriter-Regular.ttf": "87f56927f1ba726ce0591955c8b3b42d",
"assets/packages/wakelock_plus/assets/no_sleep.js": "7748a45cd593f33280669b29c2c8919a",
"assets/shaders/ink_sparkle.frag": "ecc85a2e95f5e9f53123dcaf8cb9b6ce",
"assets/shaders/stretch_effect.frag": "40d68efbbf360632f614c731219e95f0",
"canvaskit/canvaskit.js": "1e8033ea0c8c804771c1836fd07acb49",
"canvaskit/canvaskit.js.symbols": "310951580eb657840fae86f76f653452",
"canvaskit/canvaskit.wasm": "efeeba7dcc952dae57870d4df3111fad",
"canvaskit/chromium/canvaskit.js": "10c40b740080c4eb9c1e074307482d39",
"canvaskit/chromium/canvaskit.js.symbols": "2bf18b9213f9fc9fb554c3890691f57c",
"canvaskit/chromium/canvaskit.wasm": "64a386c87532ae52ae041d18a32a3635",
"canvaskit/skwasm.js": "8cc11b1079ca8735f29263baafbf330a",
"canvaskit/skwasm.js.symbols": "2a35929fae90775f43ce38f8bab1697a",
"canvaskit/skwasm.wasm": "f0dfd99007f989368db17c9abeed5a49",
"canvaskit/skwasm_heavy.js": "740d43a6b8240ef9e23eed8c48840da4",
"canvaskit/skwasm_heavy.js.symbols": "0755b4fb399918388d71b59ad390b055",
"canvaskit/skwasm_heavy.wasm": "b0be7910760d205ea4e011458df6ee01",
"canvaskit/skwasm_st.js": "9eeb36850f248a8e946442a13aaaa009",
"canvaskit/skwasm_st.js.symbols": "ca49a44a388ecfe66ba43dd851d2b76d",
"canvaskit/skwasm_st.wasm": "56c3973560dfcbf28ce47cebe40f3206",
"favicon.png": "41e5bc5ad6aab67633b4d31c0aa2b8ab",
"flutter.js": "24bc71911b75b5f8135c949e27a2984e",
"flutter.js.map": "b0053d0f522eea08c12809f1843c34c9",
"flutter_bootstrap.js": "556bf6454086fdff493567ade9892f97",
"icons/apple-touch-icon-192.png": "8cf0d5162941f467a77f023c414a1812",
"icons/Icon-192.png": "d1f96bab23c50fe5f5db429aabbac81a",
"icons/Icon-512.png": "0b1dcfc1bd6c872904999125eaf18b58",
"icons/Icon-maskable-192.png": "d1f96bab23c50fe5f5db429aabbac81a",
"icons/Icon-maskable-512.png": "0b1dcfc1bd6c872904999125eaf18b58",
"icons/loading-animation.png": "41a96047dbd2463a50c46ad3bf6ff158",
"index.html": "678361937c0f29ad51e64533db39b915",
"/": "678361937c0f29ad51e64533db39b915",
"main.dart.js": "5b377bc88fbba010f8b5c5cb7d6d34a2",
"main.dart.mjs": "4255c459c47f0ba82473c26a7b394c11",
"main.dart.wasm": "7b7d41b6e26159386678fdd29c24491a",
"manifest.json": "470ae4e11290753c4293bdc1f19f1f0b",
"pyodide/ffi.d.ts": "2a6238493fae49a02f1aaf7645ff51cc",
"pyodide/micropip-0.8.0-py3-none-any.whl": "b132a43045c127404f00f781d32f3048",
"pyodide/package.json": "4cbada0c4a062c0fb2276b64ba82f6f8",
"pyodide/packaging-24.2-py3-none-any.whl": "ba8472e04cb67139842aa03ff5921358",
"pyodide/pyodide-lock.json": "c514c0f3480fe7388346a9106cc56d95",
"pyodide/pyodide.asm.js": "889b0fc3c1115308a3c09d4236f7b075",
"pyodide/pyodide.asm.wasm": "ba116948a682d77867d1e34d9e837614",
"pyodide/pyodide.d.ts": "ef437401ba3d3acae7929082123735e7",
"pyodide/pyodide.js": "ff64396508045e9cf3c4430c9f4bde1c",
"pyodide/pyodide.mjs": "4e653c19e82f19a65269caa25faec8a0",
"pyodide/python_stdlib.zip": "ba7bdcbf412690e702e7f1e0997382ed",
"python-worker.js": "0f4298ef367c19551bc65504360365e8",
"python.js": "f16eb4c0b859a8d07fa6f3ce1b7cf773",
"splash/img/dark-1x.png": "f64824fce9ca5a76c2a624bd7d419d27",
"splash/img/dark-2x.png": "0b1dcfc1bd6c872904999125eaf18b58",
"splash/img/dark-3x.png": "ae807b0c060ac361981de61f3ad87597",
"splash/img/dark-4x.png": "1bd22698351cf0ced8b3b5d70a1b218f",
"splash/img/light-1x.png": "f64824fce9ca5a76c2a624bd7d419d27",
"splash/img/light-2x.png": "0b1dcfc1bd6c872904999125eaf18b58",
"splash/img/light-3x.png": "ae807b0c060ac361981de61f3ad87597",
"splash/img/light-4x.png": "1bd22698351cf0ced8b3b5d70a1b218f",
"version.json": "127db3a3bb4ba651d6043462d8652388"};
// The application shell files that are downloaded before a service worker can
// start.
const CORE = ["main.dart.js",
"main.dart.wasm",
"main.dart.mjs",
"index.html",
"flutter_bootstrap.js",
"assets/AssetManifest.bin.json",
"assets/FontManifest.json"];

// During install, the TEMP cache is populated with the application shell files.
self.addEventListener("install", (event) => {
  self.skipWaiting();
  return event.waitUntil(
    caches.open(TEMP).then((cache) => {
      return cache.addAll(
        CORE.map((value) => new Request(value, {'cache': 'reload'})));
    })
  );
});
// During activate, the cache is populated with the temp files downloaded in
// install. If this service worker is upgrading from one with a saved
// MANIFEST, then use this to retain unchanged resource files.
self.addEventListener("activate", function(event) {
  return event.waitUntil(async function() {
    try {
      var contentCache = await caches.open(CACHE_NAME);
      var tempCache = await caches.open(TEMP);
      var manifestCache = await caches.open(MANIFEST);
      var manifest = await manifestCache.match('manifest');
      // When there is no prior manifest, clear the entire cache.
      if (!manifest) {
        await caches.delete(CACHE_NAME);
        contentCache = await caches.open(CACHE_NAME);
        for (var request of await tempCache.keys()) {
          var response = await tempCache.match(request);
          await contentCache.put(request, response);
        }
        await caches.delete(TEMP);
        // Save the manifest to make future upgrades efficient.
        await manifestCache.put('manifest', new Response(JSON.stringify(RESOURCES)));
        // Claim client to enable caching on first launch
        self.clients.claim();
        return;
      }
      var oldManifest = await manifest.json();
      var origin = self.location.origin;
      for (var request of await contentCache.keys()) {
        var key = request.url.substring(origin.length + 1);
        if (key == "") {
          key = "/";
        }
        // If a resource from the old manifest is not in the new cache, or if
        // the MD5 sum has changed, delete it. Otherwise the resource is left
        // in the cache and can be reused by the new service worker.
        if (!RESOURCES[key] || RESOURCES[key] != oldManifest[key]) {
          await contentCache.delete(request);
        }
      }
      // Populate the cache with the app shell TEMP files, potentially overwriting
      // cache files preserved above.
      for (var request of await tempCache.keys()) {
        var response = await tempCache.match(request);
        await contentCache.put(request, response);
      }
      await caches.delete(TEMP);
      // Save the manifest to make future upgrades efficient.
      await manifestCache.put('manifest', new Response(JSON.stringify(RESOURCES)));
      // Claim client to enable caching on first launch
      self.clients.claim();
      return;
    } catch (err) {
      // On an unhandled exception the state of the cache cannot be guaranteed.
      console.error('Failed to upgrade service worker: ' + err);
      await caches.delete(CACHE_NAME);
      await caches.delete(TEMP);
      await caches.delete(MANIFEST);
    }
  }());
});
// The fetch handler redirects requests for RESOURCE files to the service
// worker cache.
self.addEventListener("fetch", (event) => {
  if (event.request.method !== 'GET') {
    return;
  }
  var origin = self.location.origin;
  var key = event.request.url.substring(origin.length + 1);
  // Redirect URLs to the index.html
  if (key.indexOf('?v=') != -1) {
    key = key.split('?v=')[0];
  }
  if (event.request.url == origin || event.request.url.startsWith(origin + '/#') || key == '') {
    key = '/';
  }
  // If the URL is not the RESOURCE list then return to signal that the
  // browser should take over.
  if (!RESOURCES[key]) {
    return;
  }
  // If the URL is the index.html, perform an online-first request.
  if (key == '/') {
    return onlineFirst(event);
  }
  event.respondWith(caches.open(CACHE_NAME)
    .then((cache) =>  {
      return cache.match(event.request).then((response) => {
        // Either respond with the cached resource, or perform a fetch and
        // lazily populate the cache only if the resource was successfully fetched.
        return response || fetch(event.request).then((response) => {
          if (response && Boolean(response.ok)) {
            cache.put(event.request, response.clone());
          }
          return response;
        });
      })
    })
  );
});
self.addEventListener('message', (event) => {
  // SkipWaiting can be used to immediately activate a waiting service worker.
  // This will also require a page refresh triggered by the main worker.
  if (event.data === 'skipWaiting') {
    self.skipWaiting();
    return;
  }
  if (event.data === 'downloadOffline') {
    downloadOffline();
    return;
  }
});
// Download offline will check the RESOURCES for all files not in the cache
// and populate them.
async function downloadOffline() {
  var resources = [];
  var contentCache = await caches.open(CACHE_NAME);
  var currentContent = {};
  for (var request of await contentCache.keys()) {
    var key = request.url.substring(origin.length + 1);
    if (key == "") {
      key = "/";
    }
    currentContent[key] = true;
  }
  for (var resourceKey of Object.keys(RESOURCES)) {
    if (!currentContent[resourceKey]) {
      resources.push(resourceKey);
    }
  }
  return contentCache.addAll(resources);
}
// Attempt to download the resource online before falling back to
// the offline cache.
function onlineFirst(event) {
  return event.respondWith(
    fetch(event.request).then((response) => {
      return caches.open(CACHE_NAME).then((cache) => {
        cache.put(event.request, response.clone());
        return response;
      });
    }).catch((error) => {
      return caches.open(CACHE_NAME).then((cache) => {
        return cache.match(event.request).then((response) => {
          if (response != null) {
            return response;
          }
          throw error;
        });
      });
    })
  );
}
